import os
import os.path
import shutil
import sys
import glob


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
    # os.chdir('/Users/muthu/Downloads/keerthi/eis_report/epa')  # DO NOT UNCOMMENT THIS LINE
    workingdir = os.getcwd()  # always run this program from within a directory named epa
    return workingdir.endswith('epa')


def dirsetup():
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
    inputdir, logdir, processeddir, outputdir = dirsetup()
    # os.chdir(inputdir)
    # workingdir = os.getcwd()  # in the input dir now
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
    else:
        print("Incorrect directory for data processing!")
        sys.exit()


def sortfiles():
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
    else:
        print("Incorrect directory for data processing!")
        sys.exit()