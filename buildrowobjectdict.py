from RowClass import Row


def buildrowobjectdict(row, rowobjectdict, year):
    """
    Method does not return anything.

    This method is called from the writefinalfile.py module.

    Method takes two parameters as input.
    1. row - this is a dictionary
    2. rowobjectdict - this is another dictionary

    Purpose of this method is to initialize a Row object with values from the row dictionary, and then add it to the
    rowobjectdict.

    For each row, a Row object is created.
    This Row object is added to the rowobjectdict, if it does not already have the same key.
    This Row object is updated with values from the row dictionary.
    """
    rowobject = Row()

    rowobject.year = year
    rowobject.state = row['addr_state_cd']  # FUTURE - check for state code in file name with data inside file.
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
    elif row.get('pollutant_cd').strip() == 'PM10-PRI':
        currobj.pmpri = row.get('total_emissions')
    elif row.get('pollutant_cd').strip() == 'SO2':
        currobj.so2 = row.get('total_emissions')
    elif row.get('pollutant_cd').strip() == 'VOC':
        currobj.voc = row.get('total_emissions')
