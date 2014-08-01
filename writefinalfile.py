import csv
from buildrowobjectdict import buildrowobjectdict

def writefinalfile(filename, finalresultfile):
    with open(filename) as f:
        finalresultfile.writelines(','.join(
            ['year', 'addr_state_cd', 'eis_facility_site_id', 'facility_site_name', '7439921', 'CO', 'NOX', 'PM-PRI',
             'SO2', 'VOC']))
        finalresultfile.writelines('\n')

        f_csv = csv.DictReader(f)
        rowobjectdict = {}

        for row in f_csv:
            buildrowobjectdict(row, rowobjectdict)

        for key in rowobjectdict.keys():
            finalresultfile.writelines(rowobjectdict[key].__str__())
            finalresultfile.writelines('\n')

        finalresultfile.close()