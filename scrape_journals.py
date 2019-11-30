import requests
from bs4 import BeautifulSoup
import mysql.connector
import re

pages = 18
base_url = 'http://portal.core.edu.au'
url = base_url+'/jnl-ranks/?search=&by=all&source=all&sort=atitle&page='


ranks = ['A*','A','B','C','Other','Not ranked']

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='12345678',
    database="FoR"
)

mycursor = mydb.cursor(buffered=True)

addjournalsql = "INSERT INTO journal (`title`,`rank`,`FoR`,`rating`) VALUES (%(Title)s,%(Rank)s,%(FoR)s,%(Rating)s)"
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
        columns = row.find_all('td')
        if not columns:
            continue

        data_journal = {
            'Title':columns[0].string.strip(),
            'Rank':ranks.index(columns[2].string.strip()),
            'FoR':int(columns[4].string.strip()),
            'Rating':get_rating(columns[6].string.strip())
        }

        mycursor.execute(searchFoRsql, (data_journal['FoR'],))
        if mycursor.rowcount == 0:
            response = requests.get(base_url+row['onclick'].split('\'')[1])
            soup_record = BeautifulSoup(response.text,"lxml")
            FoR_title = soup_record.find(text=re.compile(str(data_journal['FoR']))).split('-')[1].strip()
            mycursor.execute(addFoRsql,(data_journal['FoR'],FoR_title))

        mycursor.execute(addjournalsql,data_journal)
        mydb.commit()

mydb.close()
