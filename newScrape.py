from os import link
import winsound
import requests
from bs4 import BeautifulSoup as bs
import datetime
import pickle

updatedDate = ''
with open('date.txt', 'r+') as f:
    line = f.readline()
    line = line.split("/")
    updatedDate = line[0] + '/' + line[1] + '/' + line[2] + '/'
userInput = input("Please enter links after date DD/MM/YYYY- " + updatedDate + ": ")
links = userInput.split(", ")
links = links[0: len(links)-1]
scraped = []

with open('loginData2.pickle', 'rb') as f:
    url, login, header, login_payload = pickle.load(f)

s = requests.session()
login_req = s.post(url+login, headers=header, data=login_payload)
print(login_req)

def downloadImages(url, th):
    date = ''
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
            
            date = image['src'][image['src'].find('/20')+1:image['src'].find('/20')+11]

            with open('images/'+str(titleName.replace('.', '-')) + '--' + str(count) + ' ('+ url[8:len(url)].replace('/', '-') +') ' '.jpg', 'wb') as f:
                f.write(download.content)
            count+=1

        page +=1
        scrapeUrl = s.get(pureUrl+'/'+str(page)).url
        if (scrapeUrl == pureUrl):
            visited = True

    date = date.split("/")
    d1 = datetime.date(int(date[2]), int(date[1]), int(date[0]))

    with open('date.txt', 'r+') as f:
        line = f.readline()
        line = line.split("/")
        d2 = datetime.date(int(line[0]), int(line[1]), int(line[2]))

        if (d1 > d2):
            with open('date.txt', 'w') as file:
                file.write(d1.strftime("%d/%m/%Y"))


    return th + 1


count = 1
for url in links:
    count = downloadImages(url, count)

for skipped in scraped:
    print("Already scrapped-------------------------------------------------------" + skipped)



duration = 400  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)
