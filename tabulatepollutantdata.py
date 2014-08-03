from writefinalfile import writefinalfile
from filehandling import findos
from filehandling import getiofiledata
from filehandling import joinfiles
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
    print("Done processing all individual files.")
    print("Starting to combine files.")
    joinfiles()
    print("Finished combining files.")
    endtime = datetime.today()
    print("Process took: {} seconds".format((endtime - starttime).total_seconds()))


if __name__ == '__main__':
    main()
