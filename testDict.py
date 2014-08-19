from statistics import mean
from decimal import Decimal
import csv
from ViolationRecord import ViolationRecord


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


def createdict(aFile):
    with open(aFile) as f:
        f_csv = csv.DictReader(f)
        d = {}

        for row in f_csv:
            key = (row['eis_facility_site_id'], row['facility_site_name'], row['addr_state_cd'])
            if key not in d:
                d[key] = {}
                value = {}
                value[row['year']] = [row['7439921'], row['CO'], row['NOX'], row['PM-PRI'], row['SO2'], row['VOC']]
                d[key].update(value)
            else:
                value = {}
                value[row['year']] = [row['7439921'], row['CO'], row['NOX'], row['PM-PRI'], row['SO2'], row['VOC']]
                d[key].update(value)

        return d


def create_vr_file(aFile):
    d = createdict(aFile)

    newFile = 'violationrecords_' + aFile
    with open(newFile, 'w') as f:
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

            *remainingkeys, maxkey = allkeys

            latestdata = d[key][maxkey]

            remvalues = list(zip(*[d[key][subkey] for subkey in remainingkeys]))

            if remvalues:
                lead, co, no2, pmpri, so2, voc = remvalues
                lead, co, no2, pmpri, so2, voc = list(lead), list(co), list(no2), list(pmpri), list(so2), list(voc)
                lead, co, no2, pmpri, so2, voc = removenodata(lead), removenodata(co), removenodata(no2), removenodata(
                    pmpri), removenodata(so2), removenodata(voc)

                meandata = [findmean(lead), findmean(co), findmean(no2), findmean(pmpri), findmean(so2), findmean(voc)]
                meandata = map(str, meandata)

            vr = ViolationRecord()
            vr.efsi, vr.fsn, vr.state, vr.year = key[0], key[1], key[2], maxkey
            vr.lead_latest, vr.co_latest, vr.nox_latest, vr.pmpri_latest, vr.so2_latest, vr.voc_latest = latestdata
            if remvalues:
                vr.lead_mean, vr.co_mean, vr.nox_mean, vr.pmpri_mean, vr.so2_mean, vr.voc_mean = meandata
            vr.update_in_violation()

            f.writelines(vr.__str__())
            f.writelines('\n')
