import os
# print("Current directory is: ", os.getcwd())
# print(os.listdir(os.getcwd()))
# print("Changing directory: ", os.chdir("/home/parrot/"))
# print(os.listdir(os.getcwd()))

# from pathlib import Path
# space =  '    '
# branch = '│   '
# tee =    '├── '
# last =   '└── '
# def tree(dir_path: Path, prefix: str=''):
#     contents = list(dir_path.iterdir())
#     pointers = [tee] * (len(contents) - 1) + [last]
#     for pointer, path in zip(pointers, contents):
#         yield prefix + pointer + path.name
#         if path.is_dir():
#             extension = branch if pointer == tee else space 
#             yield from tree(path, prefix=prefix+extension)
# for line in tree(Path.home() / '/home/parrot/pysec2023/logparser_kristaps'):
#     print(line)

import os

for dirname, dirnames, filenames in os.walk('.'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        print(os.path.join(dirname, subdirname))

    # print path to all filenames.
    for filename in filenames:
        print(os.path.join(dirname, filename))

    # Advanced usage:
    # editing the 'dirnames' list will stop os.walk() from recursing into there.
    if '.git' in dirnames:
        # don't go into any .git directories.
        dirnames.remove('venv3.9')
        dirnames.remove('.git')
