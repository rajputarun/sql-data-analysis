#-- Scandinavian Institute of Business Analytics SCANBA
#-- www.scanba.org
#-- Course:
#-- SQL for Data Analysis
#-- Chapter 05: Connecting Data Analytics Software
#-- Lecture 05-06: Connecting Python

import pyodbc
import pandas

sql_server_connection = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=LB-LENOVO;'
    'Database=snp500;'
    'Trusted_Connection=yes;'
    )

dataframe=pandas.read_sql_query('SELECT * FROM [dbo].[CompanyBySector]', sql_server_connection)

print(dataframe)