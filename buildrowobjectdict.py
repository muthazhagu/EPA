from RowClass import Row


def buildrowobjectdict(row, rowobjectdict):
    rowobject = Row()

    rowobject.year = '2011'
    rowobject.state = row['addr_state_cd']
    rowobject.efsi = row['eis_facility_site_id']
    rowobject.fsn = row['facility_site_name'].replace(',', '_')

    key = rowobject.signature()

    if key not in rowobjectdict:
        currobj = rowobject
        rowobjectdict[key] = currobj
    else:
        currobj = rowobjectdict[key]

    if row.get('pollutant_cd').strip() == '7439921':
        currobj.lead = row.get('total_emissions')
    elif row.get('pollutant_cd').strip() == 'CO':
        currobj.co = row.get('total_emissions')
    elif row.get('pollutant_cd').strip() == 'NOX':
        currobj.nox = row.get('total_emissions')
    elif row.get('pollutant_cd').strip() == 'PM-PRI':
        currobj.pmpri = row.get('total_emissions')
    elif row.get('pollutant_cd').strip() == 'SO2':
        currobj.so2 = row.get('total_emissions')
    elif row.get('pollutant_cd').strip() == 'VOC':
        currobj.voc = row.get('total_emissions')
