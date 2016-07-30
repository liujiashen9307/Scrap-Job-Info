import requests
from bs4 import BeautifulSoup
import csv
key_word=input("Please type in the keywords of the job you want to apply.")
url="http://www.hoitalent.com/search?keys="+key_word+"&"
Final_Dataset=[["Job","Company","Job Type","Minimum Experience","Posted","Link"]]
for i in range(0,10):
    url=url+"page="+str(i)
    response=requests.get(url)
    content=response.content
    parser=BeautifulSoup(content,"html.parser")
    for j in range(3,13):
        select=parser.select('div.job-position-teaser')[j]
        Info=select.getText()
        Info=Info.split("\n")
        #####Website####
        Website=select.select('a')[0]
        Website="http://www.hoitalent.com"+Website.get('href')
        Required_info=[]
        index=[1,6,11,18,23]
        for each in index:
            Required_info.append(Info[each]) 
        Required_info.append(Website)
        Final_Dataset.append(Required_info)
        print("Scraping the Page Now")
print("Scraping Done")
####Write File to Csv File###
with open('Job_info.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quoting=csv.QUOTE_MINIMAL)
    for each in Final_Dataset:
        spamwriter.writerow(each)