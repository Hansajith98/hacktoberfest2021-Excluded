import os
import shutil
import sys

def changed_after_compile(java_class, java_code):
    class_file = os.path.getmtime(java_class)
    java_file  = os.path.getmtime(java_code)

    return java_file > class_file

def compile(filename):
    if not os.path.exists(f'bin/{os.path.dirname(filename)}'):
        os.makedirs(f'bin/{os.path.dirname(filename)}') # folder for binary files

    if os.path.exists(f'{filename[:-5]}.class'):
        if changed_after_compile(f'{filename[:-5]}.class', filename):
            os.system(f'javac {filename}')
            os.remove(f'bin/{filename[:-5]}.class')
            try:
                shutil.move(f'{filename[:-5]}.class', f'bin/{filename[:-5]}.class')
            except:
                pass
    else:
        os.system(f'javac {filename}')
        try:
            shutil.move(f'{filename[:-5]}.class', f'bin/{filename[:-5]}.class')
        except:
            pass

if __name__ == "__main__":
    for (root, dirs, files) in os.walk(sys.argv[1]):
        for _file in files:
            compile(f'{root}/{_file}')
