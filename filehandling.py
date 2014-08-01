import os
import os.path
import shutil
import sys


os.chdir('/Users/muthu/Downloads/keerthi/eis_report/epa')


def recreatedir(workingdir, dirname):
    if os.path.exists(os.path.join(workingdir, dirname)):
        shutil.rmtree(os.path.join(workingdir, dirname))
        os.mkdir(dirname)
    else:
        os.mkdir(dirname)


def checkworkingdir():
    workingdir = os.getcwd()
    return workingdir.endswith('epa')

if checkworkingdir():
    workingdir = os.getcwd()
    print(os.listdir(workingdir))
    recreatedir(workingdir, 'log')
    recreatedir(workingdir, 'processed')
    recreatedir(workingdir, 'output')

    print(os.listdir(workingdir))

    os.chdir('input')
    workingdir = os.getcwd()
    print(workingdir)
    print(os.listdir(workingdir))

    inputfiles = [file for file in os.listdir(workingdir) if file.endswith('.csv')]
    print(inputfiles)
else:
    print("Incorrect directory for data processing!")
    sys.exit()

