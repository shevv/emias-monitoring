# Fill the following fields:
# XXXXXXXXXXXXXXXX - medical card number
# YY-MM-DD - birth date
# specialityId: 2009 - is the coronavirus blood test doctor

import requests
import json
import webbrowser
import time

found = 0
dates = []

while found == 0:

    url = "https://emias.info/api/new-cls/eim5orch/"

    payload = "{\r\n    \"jsonrpc\": \"2.0\",\r\n    \"id\": \"\",\r\n    \"method\": \"getDoctorsInfo\",\r\n    \"params\": {\r\n        \"omsNumber\": \"XXXXXXXXXXXXXXXX\",\r\n        \"birthDate\": \"YYYY-MM-DD\",\r\n        \"specialityId\": \"2009\"\r\n    }\r\n}"
    headers = {
      'Content-Type': 'application/json',
      'User-Agent': 'emias_mobile/52100 CFNetwork/1325.0.1 Darwin/21.1.0',
      'Connection': 'keep-alive',
      'x-app': 'ios',
      'Accept': 'application/json, text/plain, */*',
      'Accept-Language': 'ru'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    pretty_json = json.loads(response.text)
    
    for result in pretty_json["result"]:
        for complexResource in result["complexResource"]:
            dates.append(complexResource)
            found = 1
    if  dates:
        found = 1
        print(dates)
        webbrowser.open("https://www.youtube.com/watch?v=C-u5WLJ9Yk4")
    
    time.sleep(30)
                    
    
