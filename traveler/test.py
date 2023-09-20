import os
for dirname, dirnames, filenames in os.walk('.'):
    for subdirname in dirnames:
        dirnames.sort()
        print(os.path.join(dirname, subdirname))
    for filename in filenames:
        filenames.sort()
        print(os.path.join(dirname, filename))
    if '.git' in dirnames:
        dirnames.remove('.git')
    if 'venv3.9' in dirnames:
        dirnames.remove('venv3.9')
    
    