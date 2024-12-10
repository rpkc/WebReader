import requests
from bs4 import BeautifulSoup

class GoogleFinance:

    def __init__(self,symbol:str):
        __code:str=symbol.upper().strip()
        url:str="https://www.google.com/finance/quote/"+__code
        result=requests.get(url)
        self.parsed_page=BeautifulSoup(result.text, 'html.parser')
        self.details=dict(name='',price=0.0,low=0.0,high=0.0,low52=0.0,high52=0.0,pe=0.0)

    def __filter(self,value:str)->str:
        value=value.replace('₹','')
        value=value.replace(',','')
        return float(value.strip())

    def __scrapper(self,class_:str)->str:
        result = self.parsed_page.find(class_=class_).get_text()    
        return result

    def __scrapper_all(self,class_:str)->list:
        result = self.parsed_page.find_all(class_=class_)
        return result

    def price(self)->float:
        try:
            return self.__filter(self.__scrapper("YMlKec fxKbKc"))
        except:
            return 0.0

    def __get_details(self)->dict:
        results = self.__scrapper_all("P6K39c")
        day_range=results[1].get_text()
        year_range=results[2].get_text()
        self.details['name']:self.__scrapper('zzDege')
        self.details['price']:self.price()
        self.details['low']:self.__filter(day_range.split('-')[0])
        self.details['high']:self.__filter(day_range.split('-')[1])
        self.details['low52']:self.__filter(year_range.split('-')[0])
        self.details['high52']:self.__filter(year_range.split('-')[1])
        self.details['pe']:float(results[5].get_text())            
        return self.details

    def get_details(self,key='all'):
        self.__get_details()
        if key=='all':
            return self.details
        elif key in self.details.keys():
            return self.details[key]
        else:
            return None    





