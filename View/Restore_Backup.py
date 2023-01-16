import socket
import pyodbc
import os
import requests

path = os.getcwd()
path_data = path + '\Quan_Ly_Dan_Cu\Data'
path += '\Quan_Ly_Dan_Cu\Data\QLCUDAN.bak'
path = 'D' + path[1:]
hostname = socket.gethostname()

def Restore():
    cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=%s;'
                      'Trusted_Connection=yes;' %hostname)
    cursor = cnxn.cursor()
    cnxn.autocommit = True
    query = " RESTORE DATABASE QLCUDAN from disk = '%s' with replace " %path
    cnxn.autocommit = False
    cursor.execute(query)
    while cursor.nextset():
        pass
    cursor.commit()

def Backup():
    cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=%s;'
                      'Database=QLCUDAN;'
                      'Trusted_Connection=yes;' %hostname)
    cursor = cnxn.cursor()
    cnxn.autocommit = True
    query = " BACKUP DATABASE QLCUDAN TO DISK = '%s'" %path
    cnxn.autocommit = False
    cursor.execute(query)
    cursor.commit()

def DownGithub():
    os.chdir(path_data)
    line = 'curl -o QLCUDAN.bak https://raw.githubusercontent.com/NguyenQuocViet42/Quan_Ly_Dan_Cu_PJ/main/Data/QLCUDAN.bak'
    os.system(line)