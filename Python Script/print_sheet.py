import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('AI_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open( ENTER THE SHEET NAME ).sheet1

pp = pprint.PrettyPrinter()

alerts = sheet.get_all_records()
pp.pprint(alerts)