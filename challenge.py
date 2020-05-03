import xlrd
import csv
import urllib.request
import datetime

local_filename, _ = urllib.request.urlretrieve('https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDd.xls')

wb = xlrd.open_workbook(local_filename)
sh = wb.sheet_by_name('Data 1')
gas_prices = open('gas_prices.csv', 'w', newline='')
wr = csv.writer(gas_prices, quoting=csv.QUOTE_ALL)
wr.writerow(sh.row_values(2))
	
for rownum in range(3, sh.nrows):
	row = sh.row_values(rownum)
	excel_date = row[0]
	python_date = datetime.datetime(*xlrd.xldate_as_tuple(excel_date, 0))
	row[0] = python_date.strftime("%Y-%m-%d")
	wr.writerow(row)

gas_prices.close()
	