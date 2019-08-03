import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import time 

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('AI_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Brainium Alerts').sheet1

pp = pprint.PrettyPrinter()

#alerts = sheet.get_all_records()
#pp.pprint(alerts)

prev_len = 0

while True:
    values_list = sheet.col_values(7)
    # pp.pprint(values_list)
    nlen = len(values_list)

    if nlen > prev_len:
        pp.pprint(values_list[-1])
		KEY = values_list[-1]
		
		if KEY == "H": #HUE
			pyautogui.keyDown('ctrl')
			pyautogui.keyDown('U')
			time.sleep(0.1)
			pyautogui.keyUp('tab')
			
		elif KEY == "L": #Level
			pyautogui.keyDown('ctrl')
			pyautogui.keyDown('L')
			time.sleep(0.1)
			pyautogui.keyUp('tab')
			
		elif KEY == "C": #Curves
			pyautogui.keyDown('ctrl')
			pyautogui.keyDown('M')
			time.sleep(0.1)
			pyautogui.keyUp('tab')
			
		elif KEY == "I": #Invert
			pyautogui.keyDown('ctrl')
			pyautogui.keyDown('I')
						
		elif KEY == "Enter": #Enter
			pyautogui.keyUp('enter')
			
		elif KEY == "Left": #Left
			pyautogui.keyUp('left')
			
		elif KEY == "Right": #Right
			pyautogui.keyUp('right')
			
		elif KEY == "up": #UP
			pyautogui.keyUp('up')
			
		elif KEY == "down": #down
			pyautogui.keyUp('down')

		elif KEY == "U": #Undo
			pyautogui.keyDown('ctrl')
			pyautogui.keyDown('z')
			
		else KEY == "invU": #Redo
			pyautogui.keyDown('shift')
			pyautogui.keyDown('ctrl')
			pyautogui.keyDown('L')
        prev_len = nlen
	time.sleep(0.1)
