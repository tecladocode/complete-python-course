# Contributing

## Building the docs

Write your documentation inside `course_contents`.

To build and serve the documentation, use this command:

```bash
watchmedo shell-command --patterns="*.md" --recursive course_contents --command="cog -r mkdocs.yml"
```

This runs the `cog -r mkdocs.yml` command every time there is a markdown file change.

**note**: at the moment there is [a bug](https://github.com/gorakhargosh/watchdog/issues/346) in `watchmedo` that triggers the shell command twice on file modification, or potentially a few times on file creation. It doesn't affect us majorly.

### Why do we need to use `cog` to build the docs before serving?

The documentation system we use for this e-book, `mkdocs`, has limitation regarding slugs: all slugs are calculated from the filesystem paths.

This means that if we simply serve the docs from `course_contents`, all our slugs would be numbered (e.g. `1_intro/lectures/3_variables_printing/`).

To avoid this, we first run a build step (in `content.py`, `build_and_get_yaml_contents()`) that copies all the non-hidden sections and lectures to a `build` folder, and then we can serve the documentation from there.

This is a bit "hacky", and we must remember to run `cog` on the `mkdocs.yml` file if we want to see our updated documentation!

## Writing documentation README files

There are a few attributes for each `README.md` file that we can use.

In section files:

- `group: str` will try to place sections with the same group name inside a tabbed navigation.
- `hidden: true | false` will hide the section and its lectures, and not include any of them in the build.

In lecture files:

- `hidden: true | false` will hide the lecture and not include it in the build. Other lectures in the same section are unaffected.
