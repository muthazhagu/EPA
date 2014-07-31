from RowClass import Row


def buildrowobjectlist(row, rowobjectlist):
    rowobject = Row()

    rowobject.year = '2011'
    rowobject.state = row['addr_state_cd']
    rowobject.efsi = row['eis_facility_site_id']
    rowobject.fsn = row['facility_site_name']

    if rowobject not in rowobjectlist:
        rowobjectlist.append(rowobject)
        currobj = rowobjectlist[-1]
    else:
        objectindex = rowobjectlist.index(rowobject)
        currobj = rowobjectlist[objectindex]

    if row.get('pollutant_cd').strip() == '7439921':
        currobj.lead.append(row.get('total_emissions'))
    elif row.get('pollutant_cd').strip() == 'CO':
        currobj.co.append(row.get('total_emissions'))
    elif row.get('pollutant_cd').strip() == 'NOX':
        currobj.nox.append(row.get('total_emissions'))
    elif row.get('pollutant_cd').strip() == 'PM-PRI':
        currobj.pmpri.append(row.get('total_emissions'))
    elif row.get('pollutant_cd').strip() == 'SO2':
        currobj.so2.append(row.get('total_emissions'))
    elif row.get('pollutant_cd').strip() == 'VOC':
        currobj.voc.append(row.get('total_emissions'))
