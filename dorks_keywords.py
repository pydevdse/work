import requests, lxml
#from lxml import html
from bs4 import BeautifulSoup as bsoup

class Dork_keywords(object):
    def __init__(self, domen):
        self.domen = domen
        
    def get_keywords(self):
        #proxies = {'http': "socks5://"+proxy}
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
        keys =['payment','visa','mastercard','buy','sell', 'invoice'] # список ключевых слов для проверки
        keywords = 'payment|visa|mastercard|buy|sell|invoice' # список ключевых слов для запроса
        domen = self.domen#'mastercard.com' # домен для поиска
        query = 'site:'+domen+' intext:'+keywords # формируем запрос
        params   = { 'q': query, 'start': 0 } # параметры запроса к гуглю
        base_url = 'https://www.google.com/search' # адрес запроса
        #proxies = {'http': "socks5://"+proxy}
        resp = requests.get(base_url, params=params,timeout=10, headers=headers) # делаем запрос #proxies=proxies
        soup = bsoup(resp.text, 'lxml')
        links = soup.findAll('div', class_="g")
        #print (len(links)) # кол-во ссылок на страницы и сслыки
        count_keywords={}
        l=0
        for decrp in links:#page: # ----------------- обрабатывем результаты на странице поиска(перебираем)
            d = decrp.find('span',class_="st")
            if d == None: continue
            #print('=============================')
            #print(d)
            
            #t = d.findAll('em')#,class_="st")#.get("em")
            #print(t)
            for k in keys:
                c = str(d).lower().count(k) 
                if c>0: # проверяем каждый элемент на нахождение нужного слова
                    #print(k)
                    if count_keywords.get(k) == None: #
                        count_keywords[k]=c
                    else:
                        count_keywords[k]+=c
        return count_keywords


r = Dork_keywords('paypal.com')
print(r.get_keywords())
