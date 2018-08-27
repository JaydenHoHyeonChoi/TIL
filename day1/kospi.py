# https://finance.naver.com/sise/에 요청을 보내서, 응답을 받아온다.


import requests
import bs4

url = "https://finance.naver.com/sise/"
response = requests.get(url)    #requests야 url이라는 애를 받아와줘(get)
# print(response.text)

html = bs4.BeautifulSoup(response.text, "html.parser")
# print(html)     # html은 이미 beautifulSoup가 특정정보를 가져오도록 정제를 해놓은 상태

kospi = html.select_one('#KOSPI_now')
print(kospi.text)
