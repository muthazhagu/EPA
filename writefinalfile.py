import csv
from buildrowobjectlist import buildrowobjectlist

def writefinalfile(filename, finalresultfile):
    with open(filename) as f:
        finalresultfile.writelines(','.join(
            ['year', 'addr_state_cd', 'eis_facility_site_id', 'facility_site_name', '7439921', 'CO', 'NOX', 'PM-PRI',
             'SO2', 'VOC']))
        finalresultfile.writelines('\n')

        f_csv = csv.DictReader(f)
        rowobjectlist = []

        for row in f_csv:
            buildrowobjectlist(row, rowobjectlist)

        for item in rowobjectlist:
            finalresultfile.writelines(item.__str__())

        finalresultfile.close()