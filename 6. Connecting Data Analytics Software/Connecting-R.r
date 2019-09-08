#-- Scandinavian Institute of Business Analytics SCANBA
#-- www.scanba.org
#-- Course:
#-- SQL for Data Analysis
#-- Chapter 05: Connecting Data Analytics Software
#-- Lecture 05-05: Connecting R

library("RODBC")

sql_server_connection <- odbcDriverConnect('Driver={SQL Server};Server=LB-LENOVO;Database=snp500;Trusted_connection=True')
dataframe <- sqlQuery(sql_server_connection, "SELECT * From [dbo].[CompanyBySector]")
print(dataframe)