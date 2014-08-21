import csv
from buildrowobjectdict import buildrowobjectdict


def writefinalfile(filename, finalresultfile, year):
    """
    :param filename: name of the input file
    :param finalresultfile: name of the output file
    :param year: year of the data
    :return: nothing

    This method creates the files in the output directory, for each file in the input directory.

    Method name is a misnomer - it really does not write the final result, but instead a file needed
    for intermediate data processing.

    """
    with open(filename) as f:
        finalresultfile.writelines(','.join(
            ['eis_facility_site_id', 'facility_site_name', 'addr_state_cd', 'year', '7439921', 'CO', 'NOX', 'PM10-PRI',
             'SO2', 'VOC']))
        finalresultfile.writelines('\n')

        f_csv = csv.DictReader(f)
        rowobjectdict = {}

        for row in f_csv:
            buildrowobjectdict(row, rowobjectdict, year)

        for key in rowobjectdict.keys():
            finalresultfile.writelines(rowobjectdict[key].__str__())
            finalresultfile.writelines('\n')

        finalresultfile.close()