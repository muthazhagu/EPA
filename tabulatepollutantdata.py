from writefinalfile import writefinalfile
import os
import sys

def findos():
    if os.name == 'posix':
        root_dir = '/'
    elif os.name == 'nt':
        root_dir = 'C:\\'
    else:
        print('Unknown OS.')
        sys.exit()


def main():
    findos()
    inputfile = '/Users/muthu/Downloads/keerthi/eis_report/results.csv'
    finalresultfile = open('/Users/muthu/Downloads/keerthi/eis_report/finalresult.csv', 'w')
    writefinalfile(inputfile, finalresultfile)


if __name__ == '__main__':
    main()
