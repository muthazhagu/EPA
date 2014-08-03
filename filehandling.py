import os
import os.path
import shutil
import sys


def findos():
    if os.name == 'posix':
        root_dir = '/'
    elif os.name == 'nt':
        root_dir = 'C:\\'
    else:
        print('Unknown OS.')
        sys.exit()


def recreatedir(workingdir, dirname):
    if os.path.exists(os.path.join(workingdir, dirname)):
        shutil.rmtree(os.path.join(workingdir, dirname))
        os.mkdir(dirname)
    else:
        os.mkdir(dirname)


def checkworkingdir():
    workingdir = os.getcwd()  # always run this program from within a directory named epa.
    return workingdir.endswith('epa')


def dirsetup():
    if checkworkingdir():
        workingdir = os.getcwd()  # must return the epa directory
        print(os.listdir(workingdir))
        recreatedir(workingdir, 'log')
        recreatedir(workingdir, 'processed')
        recreatedir(workingdir, 'output')
        print(os.listdir(workingdir))
        inputdir = os.path.join(workingdir, 'input')
        logdir = os.path.join(workingdir, 'log')
        processeddir = os.path.join(workingdir, 'processed')
        outputdir = os.path.join(workingdir, 'output')
        return inputdir, logdir, processeddir, outputdir
    else:
        print("Incorrect directory for data processing!")
        sys.exit()


def getiofiledata():
    inputdir, logdir, processeddir, outputdir = dirsetup()
    os.chdir(inputdir)
    workingdir = os.getcwd()  # in the input dir now
    print(workingdir)
    filedata = [
        (os.path.join(workingdir, file), str(file[:4]), os.path.join(outputdir, os.path.splitext(file)[0] + '_output.csv'))
        for file in os.listdir(workingdir) if file.endswith('.csv')]
    return filedata


