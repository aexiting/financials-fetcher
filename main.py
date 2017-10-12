import requests
import json
#https://api.intrinio.com/fundamentals/standardized?identifier=AAPL&statement=income_statement&type=FY
#Prints out values of the income statement on a new line.
r = requests.get("https://api.intrinio.com/financials/standardized?identifier=AAPL&statement=income_statement&fiscal_year=2015&fiscal_period=FY",auth=("bb12588db9f075e524b8f7adde230577","c54e8ba5ed9ed2fec7ff972960a90905"))

parse_json = json.loads(r.text)
for x in parse_json['data']:
  print(str(x['tag'])+":"+str(x['value']))
