from statistics import mean
from decimal import Decimal
import os
from glob import glob
import csv
from ViolationRecord import ViolationRecord


# eis_facility_site_id,facility_site_name,addr_state_cd,year,7439921,CO,NOX,PM-PRI,SO2,VOC


def removenodata(aList):
    temp = aList[:]
    for item in temp:
        if item == 'no data':
            aList.remove(item)
    return aList


def findmean(aList):
    if aList:
        aList = list(map(Decimal, aList))
        return mean(aList)
    else:
        return 'no data'


os.chdir('/Users/muthu/Downloads/keerthi/eis_report/epa/combined')


def createdict():
    with open('OH_combined_output.csv') as f:
        f_csv = csv.DictReader(f)
        d = {}

        # count = 0
        for row in f_csv:
            key = (row['eis_facility_site_id'], row['facility_site_name'])
            if key not in d:
                d[key] = {}
                value = {}
                value[row['year']] = [row['7439921'], row['CO'], row['NOX'], row['PM-PRI'], row['SO2'], row['VOC']]
                d[key].update(value)
            else:
                value = {}
                value[row['year']] = [row['7439921'], row['CO'], row['NOX'], row['PM-PRI'], row['SO2'], row['VOC']]
                d[key].update(value)

                # d[key].update(value)
                # count += 1
                # if count >= 10:
                # break

        # for k1, v1 in d.items():
        # for k2, v2 in v1.items():
        #         print(k1, '->', k2, ':', v2)

        return d


def main():
    # d = {('8191911', 'Caterpillar'): {'2000': ['1.1', '2', '3', 'no data', '5', '6'],
    # '2001': ['1.2', '2', '3', 'no data', '5', '6'],
    #                                   '2002': ['1.3', '2', '3', 'no data', 'no data', '6'],
    #                                   '2003': ['1.4', '2', '3', 'no data', '5', '6'],
    #                                   '2004': ['10', '2', '3', 'no data', '5', '6']}}

    d = createdict()

    with open('violationrecords.csv', 'w') as f:
        f.writelines(','.join(
            ['eis_facility_site_id', 'facility_site_name', 'addr_state_cd', 'year',
             '7439921_latest', '7439921_mean',
             'CO_latest', 'CO_mean',
             'NOX_latest', 'NOX_mean',
             'PM-PRI_latest', 'PM-PRI_mean',
             'SO2_latest', 'SO2_mean',
             'VOC_latest', 'VOC_mean',
             'In Violation?\n']))
        for key in d.keys():
            allkeys = list(d[key].keys())
            allkeys.sort()
            # print("All Keys ->", allkeys)

            *remainingkeys, maxkey = allkeys

            latestdata = d[key][maxkey]
            # print('Latest year\'s data')
            # print(maxkey, '->', latestdata)

            # print(len(d[key]))  # Must be 5

            remvalues = list(zip(*[d[key][subkey] for subkey in remainingkeys]))
            # print(remvalues)

            lead, co, no2, pmpri, so2, voc = remvalues
            lead, co, no2, pmpri, so2, voc = list(lead), list(co), list(no2), list(pmpri), list(so2), list(voc)
            lead, co, no2, pmpri, so2, voc = removenodata(lead), removenodata(co), removenodata(no2), removenodata(
                pmpri), \
                                             removenodata(so2), removenodata(voc)

            meandata = [findmean(lead), findmean(co), findmean(no2), findmean(pmpri), findmean(so2), findmean(voc)]
            meandata = map(str, meandata)

            # print('Mean data')
            # print(meandata)
            # print()

            vr = ViolationRecord()
            vr.efsi, vr.fsn, vr.year = key[0], key[1], maxkey
            vr.lead_latest, vr.co_latest, vr.nox_latest, vr.pmpri_latest, vr.so2_latest, vr.voc_latest = latestdata
            vr.lead_mean, vr.co_mean, vr.nox_mean, vr.pmpri_mean, vr.so2_mean, vr.voc_mean = meandata
            vr.update_in_violation()

            # print(vr)

            f.writelines(vr.__str__())
            f.writelines('\n')


if __name__ == '__main__':
    main()