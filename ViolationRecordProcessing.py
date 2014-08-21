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
    """
    :param aFile: Filename of the file containing the combined data - i.e. files in the combined dir.
    :return: A massive dictionary that contains data in this format - for example -
    {('12345', 'FacilityName'):{'2001': ['1', '2', '3', '4', '5', '6'],
                                '2002': ['1', '2', '3', 'no data', '5', '6'],
                                '2003': ['1', '2', '3', 'no data', '5', '6']
                            }
    }

    The above data structure is a dict containing a dict whose values are a list.
    The outer dict's key is the Facility ID, and the Facility Name.
    The inner dict's key is the year of the data.
    The lists contain the pollutant's concentration in tons per year.
    If there is no data for a particular year, it is represented as 'no data'

    This method may have to be reimplemented, if the data cannot fit within main memory.
    """
    with open(aFile) as f:
        f_csv = csv.DictReader(f)
        d = {}

        for row in f_csv:
            key = (row['eis_facility_site_id'], row['facility_site_name'], row['addr_state_cd'])
            if key not in d:
                d[key] = {}
                value = {}
                value[row['year']] = [row['7439921'], row['CO'], row['NOX'], row['PM10-PRI'], row['SO2'], row['VOC']]
                d[key].update(value)
            else:
                value = {}
                value[row['year']] = [row['7439921'], row['CO'], row['NOX'], row['PM10-PRI'], row['SO2'], row['VOC']]
                d[key].update(value)

        return d


def create_vr_file(aFile):
    """
    :param aFile: Combined file name, i.e. files in the combined dir.
    :return: Returns nothing.

    Inspite of its size, this method is very simple.
    All it does is, for every file in the combined dir, it creates another file containing the recommendation data.
    """

    d = createdict(aFile)

    newFile = 'followup_details_' + aFile
    with open(newFile, 'w') as f:
        f.writelines(','.join(
            ['eis_facility_site_id', 'facility_site_name', 'addr_state_cd', 'year',
             '7439921_latest', '7439921_mean',
             'CO_latest', 'CO_mean',
             'NOX_latest', 'NOX_mean',
             'PM10-PRI_latest', 'PM10-PRI_mean',
             'SO2_latest', 'SO2_mean',
             'VOC_latest', 'VOC_mean',
             'Follow-up recommended?\n']))
        for key in d.keys():
            allkeys = list(d[key].keys())
            allkeys.sort()

            *remainingkeys, maxkey = allkeys

            latestdata = d[key][maxkey]

            remvalues = list(zip(*[d[key][subkey] for subkey in remainingkeys]))

            if remvalues:
                lead, co, nox, pmpri, so2, voc = remvalues
                lead, co, nox, pmpri, so2, voc = list(lead), list(co), list(nox), list(pmpri), list(so2), list(voc)
                lead, co, nox, pmpri, so2, voc = removenodata(lead), removenodata(co), removenodata(nox), removenodata(
                    pmpri), removenodata(so2), removenodata(voc)


                meandata = [findmean(lead) + Decimal('0.6') if not findmean(lead) == 'no data' else findmean(lead),
                            findmean(co) + Decimal('100') if not findmean(co) == 'no data' else findmean(co),
                            findmean(nox) + Decimal('40') if not findmean(nox) == 'no data' else findmean(nox),
                            findmean(pmpri) + Decimal('15') if not findmean(pmpri) == 'no data' else findmean(pmpri),
                            findmean(so2) + Decimal('40') if not findmean(so2) == 'no data' else findmean(so2),
                            findmean(voc) + Decimal('40') if not findmean(voc) == 'no data' else findmean(voc)]
                meandata = map(str, meandata)

            vr = ViolationRecord()
            vr.efsi, vr.fsn, vr.state, vr.year = key[0], key[1], key[2], maxkey
            vr.lead_latest, vr.co_latest, vr.nox_latest, vr.pmpri_latest, vr.so2_latest, vr.voc_latest = latestdata
            if remvalues:
                vr.lead_mean, vr.co_mean, vr.nox_mean, vr.pmpri_mean, vr.so2_mean, vr.voc_mean = meandata
            vr.update_in_violation()

            f.writelines(vr.__str__())
            f.writelines('\n')
