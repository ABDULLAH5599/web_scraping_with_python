import csv

import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.amazon.com.au/s?k=graphics+card&crid=1CIHY51SVVZQA&sprefix=graphics%2Caps%2C322&ref=nb_sb_ss_ts-doa-p_1_8')
print(page)
soup = BeautifulSoup(page.content, 'html.parser')
contents = soup.find('div', class_='s-main-slot')


#

resultList = contents.find_all('h2', class_='a-size-mini')
ratings = soup.find_all('div', class_='a-row a-size-small')
numberRatings = soup.find_all('div', class_='a-row a-size-small')
cost = soup.find_all('div', class_='a-section a-spacing-base')






for result in resultList:
        titles = result.find('span', class_='a-size-base-plus').text

        print(titles)


for ratingResult in ratings:
    FinalResult = ratingResult.find('span', class_='a-icon-alt').text
    print(FinalResult)

for Cost in cost:
    TotalCost = Cost.find('span', class_='a-price-whole')
    print( TotalCost)
for findNumber in numberRatings:
    finalResultNumber = findNumber.find('span', class_='a-size-base s-underline-text').text
    print(finalResultNumber)


with open('sifat.csv', mode='w', newline='') as outputFile:
    amazonPrice = csv.writer(outputFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    amazonPrice.writerow(["Name"])
    amazonPrice.writerow([titles])


# this is amazon.com website ..div class information




# h2= a-size-mini
# link =a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal
# child div class =sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20
# span = a-size-base-plus a-color-base a-text-normal
# div =s-main-slot

# main div class= s-matching-dir sg-col-16-of-20 sg-col sg-col-8-of-12 sg-col-12-of-16

#  rating div
#  div class =a-row a-size-small
