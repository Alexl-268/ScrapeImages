from os import link
import winsound
import requests
from bs4 import BeautifulSoup as bs
import datetime

updatedDate = ''
with open('date.txt', 'r+') as f:
    line = f.readline()
    line = line.split("/")
    updatedDate = line[0] + '/' + line[1] + '/' + line[2] + '/'
userInput = input("Please enter links after date - " + updatedDate + ": ")
links = userInput.split(", ")
links = links[0: len(links)-1]
scraped = []

url = 'https://www.lmmpic.com'

login = '/wp-login.php'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'origin': url,
    'referer': url+login}
login_payload = {
    'log': 'sdfgkjhg1@gmail.com',
    'pwd': 'l0maNdr@',
    'testcookie': '1',
    'wp-submit': '登录',}
s = requests.session()
login_req = s.post(url+login, headers=header, data=login_payload)
print(login_req)

def downloadImages(url, th):
    pureUrl = url[0:url.find('.html')+5]
    try :
        page = int(url[url.find('.html')+6:len(url)])
    except:
        page = 1
    scrapeUrl = s.get(pureUrl+'/'+str(page)).url
    visited = False

    soup = bs(s.get(scrapeUrl).text, 'html.parser')
    titleName = soup.find("h1", {"class": "entry-title"})
    titleName = titleName.text
    date = soup.find("ul", {"class": "spostinfo"})
    date = date.text.split(" ")
    date = date[len(date)-1]
    date = date.split("/")
    date[2] = date[2][0:4]
    d1 = datetime.date(int(date[2]), int(date[1]), int(date[0]))

    with open('date.txt', 'r+') as f:
        line = f.readline()
        line = line.split("/")
        d2 = datetime.date(int(line[2]), int(line[1]), int(line[0]))

        if (d1 > d2):
            with open('date.txt', 'w') as file:
                file.write(d1.strftime("%d/%m/%Y"))

    with open('url.txt', 'r+') as f:
        if (pureUrl in f.read()):
            scraped.append(pureUrl)
            return th + 1
        else:
            f.write("\n"+pureUrl)

    count = 1
    while (visited == False):
        soup = bs(s.get(scrapeUrl).text, 'html.parser')
        im = soup.find("div", {"class": "single-content"})
        images = im.findAll('img')

        print('Title-------------------------------------------------------' + str(th) + ' of ' + str(len(links)) + '-------------------------------------------------------' + titleName)
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

    return th + 1


count = 1
for url in links:
    count = downloadImages(url, count)

for skipped in scraped:
    print("Already scrapped-------------------------------------------------------" + skipped)



duration = 400  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)
