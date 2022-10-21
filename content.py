import glob
import json
import pathlib
import shutil
import string
import markdown
from bs4 import BeautifulSoup

def get_grouped_sections(root: str = "course_contents") -> dict[str, list]:
    sections = get_all_sections_with_content(root)
    grouped_sections = {}
    for section in sections:
        group = section["index"]["group"]
        if not group:
            raise RuntimeError("Not all sections part of a group.")
        if group:
            grouped_sections.setdefault(group, []).append(section)
        else:
            grouped_sections.setdefault("default", []).append(section)
    return grouped_sections

def get_all_sections_with_content(root: str = "course_contents"):
    root_path = pathlib.Path(root)
    section_folders = [folder.name for folder in root_path.iterdir() if folder.is_dir() and folder.name[0] in string.digits]
    sections = sorted(section_folders, key=lambda e: int(str(e).split("_")[0]))
    for section in sections:
        section = root_path / section
        section_index = get_lecture_content(section / "README.md")
        if not section_index.get("title") or section_index.get("hidden"):
            continue
        lectures = get_section_lectures(section)
        lecture_contents = [get_lecture_content(lecture) for lecture in lectures]
        non_hidden_lectures = [lecture for lecture in lecture_contents if not lecture.get("hidden")]
        yield {"index": section_index, "lectures": non_hidden_lectures}


def get_section_lectures(folder: pathlib.Path | str) -> list[str]:
    """Return a list of pathlib.Path objects for all lectsures in a section folder"""
    lecture_path = pathlib.Path(folder) / "lectures"
    return sorted([folder for folder in lecture_path.glob("*/README.md")])


def get_lecture_content(lecture_path: pathlib.Path, root_path: str | pathlib.Path = "course_contents") -> dict[str, str]:
    """Return a dictionary of lecture content.
    Return a dictionary with the following keys:
    - title, the h1 from the markdown file
    - summary from the markdown metadata
    - group, to group sections together, optional
    - hidden, to hide entire sections, optional
    - filename, the name of the markdown file
    - full_path, the full path to the markdown file
    - order, the order of the lecture in the section (defaults to file name)
    - path, the path to this file relative to the root"""
    with open(lecture_path) as f:
        content = f.read()
    md = markdown.Markdown(extensions=["meta"])
    html = md.convert(content)
    soup = BeautifulSoup(html, "html.parser")
    return {
        "title": soup.find("h1").text,
        "summary": md.Meta.get("summary", ""),
        "group": md.Meta.get("group", [""])[0],
        "hidden": md.Meta.get("hidden", [""])[0] == "true",
        "filename": lecture_path.name,
        "full_path": lecture_path.absolute(),
        "order": md.Meta.get("order", [lecture_path.name])[0],
        "path": lecture_path.relative_to(root_path),
    }


def get_grouped_build_sections(root: str = "build") -> dict[str, list]:
    sections = build_and_get_yaml_contents(root)
    grouped_sections = {}
    for section in sections:
        group = section["index"]["group"]
        if not group:
            raise RuntimeError("Not all sections part of a group.")
        if group:
            grouped_sections.setdefault(group, []).append(section)
        else:
            grouped_sections.setdefault("default", []).append(section)
    return grouped_sections


def build_and_get_yaml_contents(build_path: str = "build"):
    # Delete contents of the build directory
    shutil.rmtree(build_path, ignore_errors=True)
    pathlib.Path(build_path).mkdir(parents=True, exist_ok=True)
    files = glob.glob("course_contents/*", recursive=True)
    # Copy all files (not folders) to the build directory
    for file in files:
        if pathlib.Path(file).is_file():
            shutil.copy(file, build_path)
    sections = get_all_sections_with_content()
    for section in sections:
        # Strip the leading numbers of the section folder
        old_section_name = section["index"]["full_path"].parent.name
        section_name = "_".join(old_section_name.split("_")[1:])
        pathlib.Path(build_path, section_name).mkdir(parents=True, exist_ok=True)
        # Create a directory in the build folder matching the section_name
        # Copy the README.md file from the original section to the new directory
        shutil.copyfile(section["index"]["full_path"], pathlib.Path(build_path, section_name, "README.md"))
        # Copy the lecture folders to the new directory
        section["lectures"] = list(copy_lectures_to_build_path(section, section_name, build_path=build_path))
        # Update the section index to point to the new path
        section["index"]["full_path"] = pathlib.Path(build_path, section_name, "README.md").absolute()
        section["index"]["path"] = pathlib.Path(build_path, section_name, "README.md").relative_to(build_path)
        yield section


def copy_lectures_to_build_path(section: dict, new_section_name: str, build_path: str = "build"):
    for lecture in section["lectures"]:
        lecture_name = "_".join(lecture["full_path"].parent.name.split("_")[1:])
        pathlib.Path(build_path, new_section_name, lecture_name).mkdir(parents=True, exist_ok=True)
        shutil.copyfile(lecture["full_path"], pathlib.Path(build_path, new_section_name, lecture_name, "README.md"))
        lecture["full_path"] = pathlib.Path(build_path, new_section_name, lecture_name, "README.md").absolute()
        lecture["path"] = pathlib.Path(build_path, new_section_name, lecture_name, "README.md").relative_to(build_path)
        yield lecture


if __name__ == "__main__":
    section_yaml = get_grouped_build_sections()
    print(list(section_yaml))