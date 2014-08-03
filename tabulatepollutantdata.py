from writefinalfile import writefinalfile
from filehandling import findos
from filehandling import getiofiledata
from filehandling import joinfiles


def main():
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


if __name__ == '__main__':
    main()
