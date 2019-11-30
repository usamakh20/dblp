import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.18.63",
    user="newuser",
    passwd='root',
    database="dblp"
)

mycursor = mydb.cursor(buffered=True)


journalCount = "SELECT Count(journal.name) as `publications`,journal.name " \
               "FROM journal,publication,authors_publications " \
               "WHERE authors_publications.author_id = %s AND " \
               "publication.id = authors_publications.publ_id AND " \
               "publication.journal_id=journal.id" \
               "GROUP BY journal.name"

conferencesCount = "SELECT count(*) as `publications`,publication.key" \
                   "FROM dblp.publication,authors_publications" \
                   "WHERE authors_publications.author_id = %s AND " \
                   "authors_publications.publ_id = publication.id AND " \
                   "publication.`key` like conf/% " \
                   "GROUP BY SUBSTRING_INDEX(publication.`key`,'/',2)"

journalFoR = "SELECT * " \
             "FROM dblp.journalsfor" \
             "WHERE Title LIKE %s"

conferenceFoR = "SELECT * " \
                "FROM dblp.conferences" \
                "WHERE Abrrvation in (%s)"


mycursor.execute(conferenceFoR.replace("%s","'lilog','ki'"))
