#BEGIN IMPORT STATEMENTS
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import requests
#END IMPORT STATEMENTS

#BEGIN GLOBAL VARIABLES
opts = Options()
opts.headless = True
assert opts.headless #Operating in headless mode
browser = Firefox(options=opts)
browser.get('https://cfo.asu.edu/buildingmaintenance-outages-shutdowns')
#WEBEX VARIABLES
url = "https://api.ciscospark.com/v1/messages"
message = ""
body = {
		"roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vODc0YmU4ZjAtMWMyOC0xMWVhLWJlYmQtMjk2MDA0YWI2MDdm",
		"text": message
}
headers = {
    'content-type': 'application/json',
    'authorization': 'Bearer INSERTBEARERTOKENHERE',
    'User-Agent': "JustMe",
    'Accept': "*/*",
    }
#END GLOBAL VARIABLES

#BEGIN GATHER FINDINGS
results = browser.find_elements_by_id('pData')
maintenanceEvents = results[0].text
maintenanceEvents = maintenanceEvents.split('\n')
#print(maintenanceEvents[0])
#END GATHER FINDINGS


#BEGIN TEXT PROCESSING
i = 0
while i < len(maintenanceEvents):
	if "Electrical" in maintenanceEvents[i] or "electrical" in maintenanceEvents[i]:
		message += maintenanceEvents[i - 11]
		message += "\n"
		message += maintenanceEvents[i - 10]
		message += "\n"
		message += maintenanceEvents[i - 9]
		message += "\n"
		message += maintenanceEvents[i - 9]
		message += "\n"
		message += maintenanceEvents[i - 8]
		message += "\n"
		message += maintenanceEvents[i - 7]
		message += "\n"
		message += maintenanceEvents[i - 6]
		message += "\n"
		message += maintenanceEvents[i - 4]
		message += "\n"
		message += maintenanceEvents[i - 3]
		message += "\n"
		message += maintenanceEvents[i - 2]
		message += "\n"
		message += maintenanceEvents[i - 1]
		message += "\n"
		message += maintenanceEvents[i]
		message += "\n"
	print( maintenanceEvents[i])
	i += 1
#END TEXT PROCESSING

#BEGIN SENDING PROCESSED TEXT TO WEBEX
body = {
		"roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vODc0YmU4ZjAtMWMyOC0xMWVhLWJlYmQtMjk2MDA0YWI2MDdm",
		"text": message
}
response = requests.request("POST", url, json=body, headers=headers)
#DEBUGS WEBEX API CALL
print(response.text)
#END SENDING PROCESSED TEXT TO WEBEX

browser.close()
print("End of Script")
