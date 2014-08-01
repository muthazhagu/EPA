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
    finalresultfile = open('/Users/muthu/Downloads/keerthi/eis_report/finalresult.csv', 'w')
    writefinalfile('/Users/muthu/Downloads/keerthi/eis_report/results.csv', finalresultfile)


if __name__ == '__main__':
    main()
