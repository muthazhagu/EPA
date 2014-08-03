from writefinalfile import writefinalfile
from filehandling import findos
from filehandling import getiofiledata


def main():
    findos()
    filedata = getiofiledata()
    for val in filedata:
        inputfile, year, outputfile = val
        finalresultfile = open(outputfile, 'w')
        print("Processing file: {}".format(inputfile))
        writefinalfile(inputfile, finalresultfile, year)
    print("Done processing all files.")


if __name__ == '__main__':
    main()
