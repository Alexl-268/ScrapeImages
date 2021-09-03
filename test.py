# word_freq = {}
import datetime
# # word_freq = {'is': [1, 3, 4, 8, 10],
# #              'at': [3, 10, 15, 7, 9],
# #              'test': [5, 3, 7, 8, 1],
# #              'this': [2, 3, 5, 6, 11],
# #              'why': [10, 3, 9, 8, 12]}
# word_freq["XIUREN秀人网 No.3585 Cherry绯月樱"] = []
# word_freq["XIUREN秀人网 No.3585 Cherry绯月樱"] = word_freq['XIUREN秀人网 No.3585 Cherry绯月樱'] + [1, 2, 3]
# word_freq["XIUREN秀人网 No.3585 Cherry绯月樱"] = word_freq['XIUREN秀人网 No.3585 Cherry绯月樱'] + [4]
# # Get multiple values of a key as list
# print(word_freq['XIUREN秀人网 No.3585 Cherry绯月樱'])

# import os

# with open('images/'+'test.txt', 'wb') as f:
#     f.write('download.content')

# count = 1

# def downloadImages():
#     global count
#     count = 12

# downloadImages()
# print(count)

# date = ["09","12", "2025"]
# d1 = datetime.date(int(date[2]), int(date[1]), int(date[0]))

# with open('date.txt', 'r+') as f:
#     line = f.readline()
#     line = line.split("/")
#     d2 = datetime.date(int(line[2]), int(line[1]), int(line[0]))

#     if (d1>d2):
#         with open('date.txt', 'w') as file:
#             file.write(d1.strftime("%d/%m/%Y"))   
        
with open('url.txt', 'r+') as f:
    url = 'https://www.lmmpic.com/1027041.shtml'
    if (url in f.read()):
        print("exist")
    else:
        print("no")
        f.write("yes")
