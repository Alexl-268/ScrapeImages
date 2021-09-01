from os import link
import winsound
import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.lmmpic.com'

login = '/wp-login.php'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'origin': url,
    'referer': url+login
}

login_payload = {
    'log': 'sdfgkjhg1@gmail.com',
    'pwd': 'l0maNdr@',
    'testcookie': '1',
    'wp-submit': '登录',
}

s = requests.session()
login_req = s.post(url+login, headers=header, data=login_payload)
print(login_req)
# cookies = login_req.cookies

#                   27/8
links = ['https://www.lmmpic.com/1026882.html/2', 'https://www.lmmpic.com/1026915.html/2', 'https://www.lmmpic.com/1026573.html', 'https://www.lmmpic.com/1026872.html',
         'https://www.lmmpic.com/1026878.html', 'https://www.lmmpic.com/1026914.html/3', 'https://www.lmmpic.com/1026916.html', 'https://www.lmmpic.com/1026905.html', 'https://www.lmmpic.com/1026883.html/4', ]

def downloadImages(url, th):
    pureUrl = url[0:url.find('.html')+5]
    try :
        page = int(url[url.find('.html')+6:len(url)])
    except:
        page = 1
    scrapeUrl = s.get(pureUrl+'/'+str(page)).url
    visited = False

    count = 1
    while (visited == False):
        soup = bs(s.get(scrapeUrl).text, 'html.parser')
        im = soup.find("div", {"class": "single-content"})
        images = im.findAll('img')
        titleName = soup.find("h1", {"class": "entry-title"})
        titleName = titleName.text


        print('Title------------------------------------------------------------------' + str(th) + ' of ' + str(len(links)) + '------------------------------------------------------------------' + titleName)
        for image in images:
            print("collecting " + image['src'] + '\t\t\t\t' + str(th) + ' of ' + str(len(links)))
            download = requests.get(image['src'])
            with open('images/'+str(titleName.replace('.', '-')) + '--' + str(count) + ' ('+ url[8:len(url)].replace('/', '-') +') ' '.jpg', 'wb') as f:
                f.write(download.content)
            count+=1

        page +=1
        scrapeUrl = s.get(pureUrl+'/'+str(page)).url
        if (scrapeUrl == pureUrl):
            visited = True

    return th+1


count = 1
for url in links:
    count = downloadImages(url, count)


duration = 400  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)
