import requests
from bs4 import BeautifulSoup

URL="https://www.bbc.com/news"

def get_headlines():
    responce=requests.get(URL)
    if responce.status_code !=200:
        print("the url is broken or not reachable")
        return[]
    
    soup=BeautifulSoup(responce.text,"html.parser")

    headlines=[]

    for h in soup.find_all("h2"):
        text = h.get_text().strip()
        if text and len(text) > 20:
            headlines.append(text)

    return headlines

def main():

    print("fetching headliens")
    headlines= get_headlines()
    for i,hl in enumerate(headlines[:10],start=1):
        print(f"{i}.{hl}")

if __name__=="__main__":
    main()
