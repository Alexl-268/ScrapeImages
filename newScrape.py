import winsound
import requests
from bs4 import BeautifulSoup as bs
import os
import re

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
cookies = login_req.cookies
count = 1
th = 1
skipped = []
#                   27/8
links = [33, 'https://www.lmmpic.com/1024867.html/3', 'https://www.lmmpic.com/1024873.html', 16, 'https://www.lmmpic.com/1024868.html/2',
         41,'https://www.lmmpic.com/1024870.html/3',  ]
#----------------------------- Asks for links
# link = input("Link: ")
# while (link != 'y'):
#     links.append(link)
#     link = input("Link: ")
# print(links)
# while (input("Do you want to continue? ") == 'y'):
#     print("Collecting Images")
#     break


def downloadImages(url, count):
  #Error Checking
    global th
    url = url[0:url.find('.html')+5]
    #Collecting image html
    soup = bs(s.get(url).text, 'html.parser')
    im = soup.find("div", {"class": "single-content"})
    images = im.findAll('img')
    titleName = soup.find("h1", {"class": "entry-title"})
    titleName = titleName.text

    print(titleName)
    print(images)


#start to download from this number of images
for url in links:
    if isinstance(url, (int, float)) == True:
        count = url
    else:
        downloadImages(url, count)
        count = 1


# print(skipped)
# duration = 400  # milliseconds
# freq = 440  # Hz
# winsound.Beep(freq, duration)


# os.system("shutdown /s /t 120")

#Colecting the image links
# image = images[0]
# imageLink = image['src']

# if imageLink[imageLink.find('.jpg')-2:imageLink.find('.jpg')] == '-1':
#      imageLink = imageLink[0:imageLink.find('.jpg')-1]
#       download = requests.get(imageLink+str(count)+'.jpg')

#        #write the images
#        while (download.status_code != 404):
#             print(str(th) + '/' + str(len(links)) +
#                   '  Collecting ' + str(url) + ' ----- ' + str(count))
#             with open(str(titleName.replace('.', '-')) + '--' + str(count) + '.jpg', 'wb') as f:
#                 f.write(download.content)

#             count = count + 1
#             download = requests.get(imageLink+str(count)+'.jpg')

#         th = th + 1
# else:
#     skipped.append(url)
