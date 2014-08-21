from writefinalfile import writefinalfile
from filehandling import findos
from filehandling import getiofiledata
from filehandling import joinfiles
from filehandling import sortfiles
from filehandling import vrfiles
from datetime import datetime


def main():
    """
    Method does not return anything.

    This is the main program that must be run.

    To run this program, type python tabulatepollutantdata.py at the command line.

    This program calls a number of methods in other modules.

    The flow of this program is as follows -
    1. It checks to see if the os is a recognized os - posix, or nt (Windows)
    2. For every file in the input dir, it creates an output file in the output dir.
    3. It then combines the files in the output dir (based on state), into a single file,
    this is the combined file, per state.
    4. For every combined file, it creates a file containing a recommendation of Y or N
    (with other relevant data). This is the file that one can review, and take further action.

    It also prints the time taken to complete the above process.
    """
    starttime = datetime.today()
    findos()
    filedata = getiofiledata()
    for val in filedata:
        inputfile, year, outputfile = val
        finalresultfile = open(outputfile, 'w')
        print("Processing file: {}".format(inputfile))
        writefinalfile(inputfile, finalresultfile, year)
    print("Done processing individual files.")
    print("Combining files.")
    joinfiles()
    print("Finished combining files.")
    # print("Sorting files.")
    # sortfiles()
    # print("Finished sorting files.")
    print("Writing recommendation records.")
    vrfiles()
    print("Finished writing recommendation records.")
    endtime = datetime.today()
    print("Process took: {} seconds".format((endtime - starttime).total_seconds()))


if __name__ == '__main__':
    main()
