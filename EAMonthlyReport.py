'''
This program will run on monthly basis and colect total archive
and retreives for each PACS Customer.
'''
import pyodbc

def ea_monthly_report():
    '''
    This function will doule 5 tasks:
    1.  Connect to SQL Server.
    2.  Run querry and retreive data from SQL server Data Base.
    3.  Write the data to Excell worksheet.
    4.  Email the worksheet to end user.
    '''
    #Define data base connection parameters
    # sqlserver = '192.168.17.128'
    # db = 'DCMARCH4'
    # username = 'asp1\\administrator'
    # password = 'Bosnia66s'
    #Establish DB connections
    conn = pyodbc.connect(
        r'DRIVER={ODBC Driver 13 for SQL Server};'
        r'SERVER=192.168.17.128;'
        r'DATABASE=DCMARCH4;'
        r'UID=administrator;'
        r'PWD=Bosnia66s'
        )
    cur = conn.cursor()
    cur.execute("""
                select FirstArchiveDate
                from tbldicomstudy
                """)
    rows = cur.fetchall()

    for row in rows:
        print(row.FirstArchiveDate)

    cur.close()
    conn.close()

#Run program
ea_monthly_report()




