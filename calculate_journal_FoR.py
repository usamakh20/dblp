import mysql.connector
from collections import Counter

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database="dblp"
)

mycursor = mydb.cursor(buffered=True)

queryjournals = "SELECT * FROM journal"

queryCoreJournals = "SELECT * FROM core_journal WHERE title LIKE %s"

mycursor.execute(queryjournals)

journals = mycursor.fetchall()

higgest_match = Counter()
for journal in journals:
    mycursor.execute(queryCoreJournals, (journal[1].replace(' ', '%') + '%',))
    if mycursor.rowcount > 0:
        for match in mycursor:
            higgest_match[match[0]] = len(match[1]) - len(journal[1])
        print(journal[1], ":", higgest_match.most_common()[-1])
        higgest_match.clear()

mycursor.close()
mydb.close()
