from writefinalfile import writefinalfile
from filehandling import findos
from filehandling import getiofiledata
from filehandling import joinfiles
from filehandling import sortfiles
from filehandling import vrfiles
from datetime import datetime


def main():
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
    print("Writing violation records.")
    vrfiles()
    print("Finished writing violation records.")
    endtime = datetime.today()
    print("Process took: {} seconds".format((endtime - starttime).total_seconds()))


if __name__ == '__main__':
    main()
