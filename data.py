import requests

class Data():
    def __init__(self,symbol, num):
        marketstack_access_key = 'cb8e140d21e76bdc2949daa2fcc836c8'
        self.symbol = symbol
        self.num = num
        self.parameter = {
            'access_key': marketstack_access_key,
            'symbols': self.symbol,
            'limit': self.num
        }
        results = requests.get(url = "http://api.marketstack.com/v1/eod", params=self.parameter)
        self.response = results.json()['data']
