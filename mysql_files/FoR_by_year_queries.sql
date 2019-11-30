CREATE TEMPORARY TABLE journal_FoR_count AS
SELECT FoR_id,year,COUNT(*) as count
FROM journal,publication
WHERE journal_id IS NOT NULL AND FoR_id IS NOT NULL AND journal_id=journal.id
GROUP BY FoR_id,year;

CREATE TEMPORARY TABLE conference_FoR_count AS
SELECT FoR_id,year,COUNT(*) as count
FROM conference INNER JOIN publication ON acronym = UPPER(SUBSTRING_INDEX(SUBSTRING_INDEX(`key`,'/',2),'/',-1))
WHERE FoR_id IS NOT NULL AND `key` like 'conf/%'
GROUP BY For_id,year;

CREATE TEMPORARY TABLE journal_FoR_count1 AS SELECT * FROM journal_FoR_count;
CREATE TEMPORARY TABLE conference_FoR_count1 AS SELECT * FROM conference_FoR_count;

CREATE TEMPORARY TABLE result AS
SELECT journal_FoR_count.FoR_id,journal_FoR_count.year,IF(conference_FoR_count.count IS NULL, journal_FoR_count.count, journal_FoR_count.count+conference_FoR_count.count) AS count 
FROM journal_FoR_count LEFT JOIN conference_FoR_count
ON journal_FoR_count.FoR_id = conference_FoR_count.FoR_id AND journal_FoR_count.year = conference_FoR_count.year
UNION
SELECT conference_FoR_count1.FoR_id,conference_FoR_count1.year,IF(journal_FoR_count1.count IS NULL, conference_FoR_count1.count, journal_FoR_count1.count+conference_FoR_count1.count) AS count 
FROM journal_FoR_count1 RIGHT JOIN conference_FoR_count1
ON journal_FoR_count1.FoR_id = conference_FoR_count1.FoR_id AND journal_FoR_count1.year = conference_FoR_count1.year;

SELECT id,name,year,count FROM result INNER JOIN focus_of_research ON FoR_id = focus_of_research.id;