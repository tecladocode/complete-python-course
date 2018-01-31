from ..json_operations import dict_to_json


def save_to_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

print(f'file_operations is {__name__}')#
