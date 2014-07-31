from writefinalfile import writefinalfile


def main():
    finalresultfile = open('/Users/muthu/Downloads/keerthi/eis_report/finalresult.csv', 'w')
    writefinalfile('/Users/muthu/Downloads/keerthi/eis_report/results.csv', finalresultfile)


if __name__ == '__main__':
    main()
