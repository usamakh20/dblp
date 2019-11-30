import requests
from bs4 import BeautifulSoup
import mysql.connector
import re

pages = 33
base_url = 'http://portal.core.edu.au'
url = base_url+'/conf-ranks/?search=&by=all&source=CORE2018&sort=atitle&page='


ranks = ['A*','A','B','C','Other','Unranked','Australasian']

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='12345678',
    database="FoR"
)

mycursor = mydb.cursor(buffered=True)

addconferencesql = "INSERT INTO conference (`title`,`acronym`,`rank`,`FoR`,`rating`) VALUES (%(Title)s,%(Acronym)s,%(Rank)s,%(FoR)s,%(Rating)s)"
addFoRsql = "INSERT INTO `FoR` (`id`,`name`) VALUES (%s,%s)"

searchFoRsql = "SELECT id FROM `FoR` WHERE id = %s"


def get_rating(string):
    if string == 'N/A':
        return None
    else: return int(float(string))

for page in range(1,pages+1):
    response = requests.get(url+str(page))
    soup = BeautifulSoup(response.text, "lxml")
    rows = soup.table.find_all('tr')
    headers = rows[0].find_all('th')

    for row in rows:
        try:
            columns = row.find_all('td')
            if not columns:
                continue

            data_conference = {
                'Title':columns[0].string.strip(),
                'Acronym':columns[1].string.strip(),
                'Rank':ranks.index(columns[3].string.strip()),
                'FoR':int(columns[5].string.strip()),
                'Rating':get_rating(columns[7].string.strip())
            }

            mycursor.execute(searchFoRsql, (data_conference['FoR'],))
            if mycursor.rowcount == 0:
                response = requests.get(base_url+row['onclick'].split('\'')[1])
                soup_record = BeautifulSoup(response.text,"lxml")
                FoR_title = soup_record.find(text=re.compile(str(data_conference['FoR']))).split('-')[1].strip()
                mycursor.execute(addFoRsql,(data_conference['FoR'],FoR_title))

            mycursor.execute(addconferencesql,data_conference)
            mydb.commit()
        except:
            print('Exception occurred')

mydb.close()
