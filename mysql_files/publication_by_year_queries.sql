SELECT * 
FROM journal INNER JOIN core_journal ON title like CONCAT(REPLACE(name,' ','%'),'%');

SELECT * FROM core_journal WHERE title LIKE 'Simulation%Modelling%Practice%and%Theory%';

INSERT INTO conference (acronym)
SELECT UPPER(SUBSTRING_INDEX(SUBSTRING_INDEX(`key`,'/',2),'/',-1))
FROM publication WHERE `key` like 'conf/%' 
GROUP BY UPPER(SUBSTRING_INDEX(SUBSTRING_INDEX(`key`,'/',2),'/',-1))
ORDER BY UPPER(SUBSTRING_INDEX(SUBSTRING_INDEX(`key`,'/',2),'/',-1));

SELECT conference.acronym,core_conference.FoR_id 
FROM dblp.conference LEFT JOIN core_conference ON conference.acronym = core_conference.acronym 
GROUP BY conference.acronym 
ORDER BY conference.id;

SELECT journal.id,journal.name,year,COUNT(*) as count
FROM publication INNER JOIN journal ON journal_id=journal.id
WHERE journal_id IS NOT NULL
GROUP BY journal_id,year
ORDER BY journal_id,year;

SELECT * 
FROM publication INNER JOIN journal ON journal_id=journal.id 
WHERE FoR_id=807 AND year=2018;

SELECT * 
FROM publication INNER JOIN conference ON acronym = UPPER(SUBSTRING_INDEX(SUBSTRING_INDEX(`key`,'/',2),'/',-1)) 
WHERE `key` like 'conf/%' AND FoR_id=913 AND year=2006;

SELECT conference.id,conference.acronym,year,COUNT(*) AS count
FROM conference,publication
WHERE `key` like 'conf/%' AND acronym = UPPER(SUBSTRING_INDEX(SUBSTRING_INDEX(`key`,'/',2),'/',-1))
GROUP BY conference.id,year
ORDER BY conference.id,year;

SELECT * 
FROM publication 
WHERE UPPER(SUBSTRING_INDEX(SUBSTRING_INDEX(`key`,'/',2),'/',-1)) = 'IGARSS' AND year=2018;

SELECT year,COUNT(*) AS count 
FROM publication 
WHERE year IS NOT NULL 
GROUP BY year;