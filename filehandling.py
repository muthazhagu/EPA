import os
import os.path
import shutil
import sys
import glob
from ViolationRecordProcessing import create_vr_file


"""
This module has a number of methods that help with file handing.

Essentially, it sets up the directories needed for the tabulatepollutantdata.py program to run.
"""

def findos():
    """
    Method does not return anything.
    If the OS is neither posix based, nor Windows, the program will quit.
    """
    if os.name == 'posix':
        root_dir = '/'
    elif os.name == 'nt':
        root_dir = 'C:\\'
    else:
        print('Unknown OS.')
        sys.exit()


def checkworkingdir():
    """
    Method return True or False, depending on whether the directory from which
    this program is run called epa (small-case).
    """
    # os.chdir('/Users/muthu/Downloads/keerthi/eis_report/epa')  # DO NOT UNCOMMENT THIS LINE
    workingdir = os.getcwd()  # always run this program from within a directory named epa
    return workingdir.endswith('epa')


def recreatedir(workingdir, dirname):
    """
    :param workingdir: workingdir in most cases must be called epa. Every other dir will be a sub-dir of epa.
    :param dirname: Any of the other dirs needed for this program. dirname is a sub-dir of epa.
    :return: Program returns nothing.
    """
    if os.path.exists(os.path.join(workingdir, dirname)):
        shutil.rmtree(os.path.join(workingdir, dirname))
        os.mkdir(dirname)
    else:
        os.mkdir(dirname)


def dirsetup():
    """
    :return: Returns the path to the dir containing the input files, path to the log dir,
    processed dir, and the output dir.

    If the working directory is not epa, the program will exit.
    """
    if checkworkingdir():
        workingdir = os.getcwd()  # must return the epa directory
        recreatedir(workingdir, 'log')
        recreatedir(workingdir, 'processed')
        recreatedir(workingdir, 'output')
        inputdir = os.path.join(workingdir, 'input')
        logdir = os.path.join(workingdir, 'log')  # FUTURE: if logging is needed, then store store logs here
        processeddir = os.path.join(workingdir, 'processed')  # FUTURE: move processed files into this directory
        outputdir = os.path.join(workingdir, 'output')
        return inputdir, logdir, processeddir, outputdir
    else:
        print("Incorrect directory for data processing!")
        sys.exit()


def getiofiledata():
    """
    :return: Method returns a list containing
    the absolute path to the input file
    - e.g.: /path/to/input/IL_results_2001.csv,

    Year of the file - e.g. 2001, and

    the absolute path to the output file
    - e.g.: /path/to/output/IL_results_2001_output.scv

    for every *.csv file in the input directory.
    """
    inputdir, logdir, processeddir, outputdir = dirsetup()
    filedata = [
        (os.path.join(inputdir, file), os.path.splitext(file)[0][-4:],
         os.path.join(outputdir, os.path.splitext(file)[0] + '_output.csv'))
        for file in os.listdir(inputdir) if file.endswith('.csv')]
    if filedata:
        return filedata
    else:
        print('No files to process.')
        sys.exit()


def joinfiles():
    """
    Method does not return anything.

    It combines all the output files into a single combined output file.

    If a state has data for 2001, 2002, and 2003 as separate output files,
    this method combines all of it, and produces a single file containing data from
    2001, 2002, and 2003.

    Individual output files are picked up from the output dir.
    Combined files are written into the combined dir.
    Combined have a file name like IL_comcbined_output.csv.
    """
    if checkworkingdir():
        workingdir = os.getcwd()  # must return the epa directory
        recreatedir(workingdir, 'combined')
        combineddir = os.path.join(workingdir, 'combined')
        os.chdir(os.path.join(workingdir, 'output'))  # In the output directory

        statenames = [file[0:2] for file in glob.glob('*.csv')]
        statenames.sort()
        statenames = set(statenames)

        for state in statenames:
            # print("State: ", state)
            sourcefilenames = glob.glob(state + '*')
            # print("Source filenames: ", sourcefilenames)
            destfilename = '_'.join([state, 'combined_output.csv'])
            # print("Destination filename: ", destfilename)
            with open(os.path.join(combineddir, destfilename), 'a') as dest:
                with open(sourcefilenames[0]) as f:
                    for line in f.readlines():
                        dest.writelines(line)
                    for source in sourcefilenames[1:]:
                        # print("Source: ", source)
                        with open(source) as f:
                            header = f.readline()  # Skip the header from the second file onwards
                            for line in f.readlines():
                                dest.writelines(line)
        os.chdir(workingdir)
    else:
        print("Incorrect directory for data processing!")
        sys.exit()


def sortfiles():
    """
    Method does not return anything.
    It does a lexical sort of the contents of each file in the combined dir.

    This method is NOT being called in the tabulatepollutantdata.py file.
    """
    if checkworkingdir():
        workingdir = os.getcwd()  # must return the epa directory
        combineddir = os.path.join(workingdir, 'combined')
        os.chdir(combineddir)

        for file in glob.glob('*.csv'):
            with open(file) as source:
                with open('sorted_' + file, 'w') as target:
                    lines = source.readlines()
                    header, *data = lines
                    data.sort()
                    target.writelines(header)
                    for line in data:
                        target.writelines(line)
        os.chdir(workingdir)
    else:
        print("Incorrect directory for data processing!")
        sys.exit()


def vrfiles():
    """
    Method does not return anything.

    For every file in the combined dir, this file creates another file called, for example -
    followup_details_IL_combined_output.csv
    """
    if checkworkingdir():
        workingdir = os.getcwd()  # must return the epa directory
        combineddir = os.path.join(workingdir, 'combined')
        os.chdir(combineddir)

        for file in glob.glob('*.csv'):
            create_vr_file(file)

        os.chdir(workingdir)
    else:
        print("Incorrect directory for data processing ->", os.getcwd())
        sys.exit()