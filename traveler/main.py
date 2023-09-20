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
import glob
#for dirname, dirnames, filenames in os.walk('.'):
    #for subdirname in dirnames:
    #    print(os.path.join(dirname, subdirname))
    #for filename in filenames:
    #    print(os.path.join(dirname, filename))
    #if '.git' in dirnames:
    #    dirnames.remove('.git')
   # if 'venv3.9' in dirnames:
   #     dirnames.remove('venv3.9')
    # files = glob.glob("dir/**/*")
    # files.sort(key=os.path.getmtime)
    # print("\n".join(files))
path = os.walk('.')
for root, dirs, files in os.walk('.'):
    print(root)
dirs[:] = [d for d in dirs if not d.startswith('-')]
for dir in dirs:
    print(os.path.join(root, dir))
for file in files:
    print(os.path.join(root, file))
#list_of_files = sorted( filter( os.path.isfile, glob.glob('dir_name' + '/**/*', recursive=True)))
#for file_path in list_of_files:
#    print(file_path) 