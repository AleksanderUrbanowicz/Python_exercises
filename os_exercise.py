import os
from datetime import datetime


def print_dir(all=False):
    print(f'Path: {os.getcwd()}')
    print(f'List: {os.listdir()}')
    if all:
        for dirpath, dirnames, filenames in os.walk(os.getcwd()):
            print(f'Path: {dirpath}')
            print(f'DirNames: {dirnames}')
            print(f'FileNames: {filenames}')


def create_dir(path_to_dir, name):
    try:
        os.chdir(path_to_dir)
    except FileNotFoundError:
        print(f'Path {path_to_dir} does not exist, returning')
        return

    try:
        os.mkdir(name)
    except FileExistsError:
        print(f'Directory {name} already exists')
    print_dir()


def rename_dir(name, new_name):
    try:
        os.rename(name, new_name)
    except FileNotFoundError:
        print(f'Directory {name} does not exist')
    print_dir()


def remove_dir(name):
    try:
        os.rmdir(name)
    except FileNotFoundError:
        print(f'Directory {name}  does not exist')
    print_dir()


def create_file(path_to_dir, name):
    try:
        os.chdir(path_to_dir)
    except FileNotFoundError:
        print(f'Path {path_to_dir} does not exist, returning')
    try:
        f = open(name, 'w+')
    except FileExistsError:
        print(f'File {name} already exists')
    finally:
        f.close()
        print_dir()


def get_file_details(path_to_dir, name):
    try:
        os.chdir(path_to_dir)
    except FileNotFoundError:
        print(f'Path {path_to_dir} does not exist, returning')

    try:
        print(f'Stats: {os.stat(name)}')
        print(f'Mod time: {datetime.fromtimestamp(os.stat(name).st_mtime)}')
    except FileNotFoundError:
        print(f'File {name} does not exist, returning')


def get_env_variable(env_var=''):
    if env_var == '':
        print(f'Env_vars: {os.environ}')
    else:
        print(f'Env_var[{env_var}]: {os.environ.get(env_var)}')


dir_path = os.path.join(os.environ.get('HOME'), 'Desktop/Test/')
dir_name = 'newDir'
new_dir_name = 'newDirRenamed'
file_name = 'testFile.txt'
# print_dir()

create_dir(dir_path, dir_name)
rename_dir(dir_name, new_dir_name)
remove_dir(new_dir_name)
create_file(dir_path, file_name)
get_file_details(dir_path, file_name)
get_env_variable()
get_env_variable('HOME')