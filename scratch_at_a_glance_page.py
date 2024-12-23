import requests
import re

cookies = {
    'ASP.NET_SessionId': 'ldjdjlmkqnizy1d51muqpbzs',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json; charset=utf-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://tis.nhai.gov.in',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://tis.nhai.gov.in/tollplazasataglance.aspx?language=en',
    # 'Cookie': 'ASP.NET_SessionId=ldjdjlmkqnizy1d51muqpbzs',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

data = '{\'TollName\':\'\'}'

response = requests.post('https://tis.nhai.gov.in/TollPlazaService.asmx/GetTollPlazaInfoGrid', cookies=cookies, headers=headers, data=data)

# Create a list
result_list = re.findall('javascript:TollPlazaPopup\(\d+\)',response.text)
ids = [int(re.findall('\d+',str_)[0]) for str_ in result_list]
print(ids)
