SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(dblp.publication.key,'/',2),'/',-1) as `acronym`,COUNT(*) as `count`
FROM dblp.authors_publications,dblp.publication
WHERE authors_publications.author_id = 3 AND authors_publications.publ_id = publication.id AND publication.key LIKE 'conf/%'
GROUP BY SUBSTRING_INDEX(SUBSTRING_INDEX(dblp.publication.key,'/',2),'/',-1);


SELECT *
FROM `FoR`.journal, (SELECT journal.id as `dblp_id`,dblp.journal.name,Count(*) AS `count`
FROM dblp.authors_publications,dblp.publication,dblp.journal
WHERE authors_publications.author_id = 271121 AND authors_publications.publ_id = publication.id
AND publication.journal_id = journal.id
group by journal.id) as result
WHERE title like CONCAT(REPLACE(REPLACE(result.name,'.',''),' ','%'),'%') 
GROUP BY dblp_id
ORDER by dblp_id,length(title);

SELECT author_id,Count(*) as `publications` 
FROM dblp.authors_publications 
GROUP BY author_id 
HAVING COUNT(*)>200 
ORDER BY COUNT(*) DESC;