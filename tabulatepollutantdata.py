from writefinalfile import writefinalfile
from filehandling import findos
from filehandling import getiofiledata
import os


def main():
    os.chdir('/Users/muthu/Downloads/keerthi/eis_report/epa')
    findos()
    filedata = getiofiledata()
    for val in filedata:
        inputfile, year, outputfile = val
        finalresultfile = open(outputfile, 'w')
        writefinalfile(inputfile, finalresultfile, year)


if __name__ == '__main__':
    main()
