import gspread

json_file = 'table.json'
gc = gspread.service_account(filename=json_file)
sh = gc.open('Test posv')

worksheet = sh.worksheet('ras')
a = worksheet.get_all_records()
print(a)