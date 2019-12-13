from lxml import etree
import mysql.connector
from datetime import datetime
import unicodedata

ELEMENTS = ['article', 'inproceedings', 'proceedings', 'book', 'incollection', 'phdthesis', 'mastersthesis', 'www']
SUB_ELEMENTS = ['author', 'editor', 'title', 'booktitle', 'pages', 'year', 'address', 'journal', 'volume', 'number',
                'month', 'url', 'ee', 'cdrom', 'cite', 'publisher', 'note', 'crossref', 'isbn', 'series', 'school',
                'chapter', 'publnr']
ATTRIBUTES = ['key', 'mdate', 'publtype', 'reviewid', 'rating', 'cdate']

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
         'December']

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='Usama1234',
    database="dblp"
)

mycursor = mydb.cursor(buffered=True)

addpublicationsql = "INSERT INTO publication (`key`, title, address, year,`type`,`mdate`,`publtype`,`rating`,`reviewid`,`cdate`, pages, volume, number, month, url, school, publisher, crossref, isbn, chapter, series,`booktitle`,`journal_id`) " \
                    "VALUES (%(key)s, %(title)s, %(address)s, %(year)s,%(type)s,%(mdate)s,%(publtype)s,%(rating)s,%(reviewid)s,%(cdate)s, %(pages)s, %(volume)s, %(number)s, %(month)s, %(url)s, %(school)s, %(publisher)s, %(crossref)s, %(isbn)s, %(chapter)s, %(series)s,%(booktitle)s,%(journal_id)s)"

addeesql = "INSERT INTO ee (url,`publ_id`) VALUES (%s,%s)"

addcitessql = "INSERT INTO cite (cite_key,`publ_id`) VALUES (%s,%s)"

addjournalsql = "INSERT INTO journal (name) VALUES (%s)"

addauthorssql = "INSERT INTO authors (name,`bibtex`) VALUES (%s,%s)"

addauthorpublicationsql = "INSERT INTO authors_publications (author_id,`publ_id`) VALUES (%s,%s)"

searchauthorsql = "SELECT id FROM authors WHERE name = %s"

searchjournalsql = "SELECT id FROM journal WHERE name = %s"

# key: journals/robotica/Owen90o
# title: The Complexity of Robot Motion Planning by John F. Canny The MIT Press, 1988, 198 pages with index (24.75).
count = 0

for event, elem in etree.iterparse('dblp.xml', load_dtd=True, encoding='utf-8'):
    if elem.tag in ELEMENTS:
        enable = True

        # Insert Publication information
        data_publication = {
            'key': elem.get('key'),
            'type': ELEMENTS.index(elem.tag),
            'publtype': None,
            'title': None,
            'address': None,
            'year': None,
            'mdate': None,
            'rating': None,
            'reviewid': None,
            'cdate': None,
            'pages': None,
            'volume': None,
            'number': None,
            'month': None,
            'url': None,
            'school': None,
            'publisher': None,
            'crossref': None,
            'isbn': None,
            'chapter': None,
            'series': None,
            'booktitle': None,
            'journal_id': None
        }

        data_ee = []

        data_journal = []

        data_author = []

        data_author_publication = []

        data_cite = []

        for attribute in elem.keys():
            value = elem.get(attribute)
            if attribute == 'mdate' or attribute == 'cdate':
                value = datetime.strptime(value, '%Y-%m-%d').date()

            elif attribute == 'reviewid':
                value = int(value)

            if type(value) == str:
                value = value.replace('\n', '')
                value = value.replace('\t', '')

            data_publication[attribute] = value

        for e in SUB_ELEMENTS:
            data = elem.findall(e)

            if not data:
                continue

            if e == 'ee':
                for d in data:
                    data_ee.append(d.text)

            elif e == 'journal':
                for d in data:
                    mycursor.execute(searchjournalsql, (d.text,))
                    if mycursor.rowcount == 0:
                        mycursor.execute(addjournalsql, (d.text,))
                        data_publication['journal_id'] = mycursor.lastrowid
                    else:
                        data_publication['journal_id'] = mycursor.fetchone()[0]

            elif e == 'author':
                for d in data:
                    mycursor.execute(searchauthorsql, (d.text,))
                    if mycursor.rowcount == 0:
                        mycursor.execute(addauthorssql, (d.text, d.get('bibtext')))
                        data_author_publication.append(mycursor.lastrowid)
                    else:
                        data_author_publication.append(mycursor.fetchone()[0])

            elif e == 'cite':
                for d in data:
                    if d.text != '...':
                        data_cite.append(d.text)

            elif e == 'month':
                try:
                    data_publication[e] = month.index(data[0].text)
                except:
                    print("Error saving month")

            elif e in ['year', 'chapter']:
                data_publication[e] = int(data[0].text)

            else:
                cleaned = unicodedata.normalize('NFKD',
                                                etree.tostring(data[0], method='text', encoding='unicode')).encode(
                    'ascii', 'ignore').decode('ascii')
                cleaned = cleaned.replace('\n', '')
                cleaned = cleaned.replace('\t', '')
                data_publication[e] = cleaned

        mycursor.execute(addpublicationsql, data_publication)
        latest_publication_id = mycursor.lastrowid
        ee = []
        for data in data_ee:
            ee.append((data, latest_publication_id))
        mycursor.executemany(addeesql, list(set(ee)))

        author_publication = []
        for data in data_author_publication:
            author_publication.append((data, latest_publication_id))
        mycursor.executemany(addauthorpublicationsql, list(set(author_publication)))

        cite = []
        for data in data_cite:
            cite.append((data, latest_publication_id))
        mycursor.executemany(addcitessql, list(set(cite)))
        mydb.commit()

        elem.clear()
        count += 1
        print("Count: " + str(count) + " ")
        print('key: ' + data_publication['key'])

mydb.close()
