TRUNCATE TABLE auth_publ;

INSERT INTO auth_publ
SELECT author_id,publ_id
FROM dblp.for_authors, dblp.authors_publications
WHERE dblp.for_authors.for_id=913 and
for_authors.id = author_id;

-- INSERT INTO coauthors_publications
SELECT distinct
case when A.author_id < B.author_id then A.author_id else B.author_id end as `author1`,
case when A.author_id > B.author_id then A.author_id else B.author_id end as `author2`,
count(A.publ_id) as `publications`
FROM dblp.authors_publications as A, dblp.authors_publications as B
WHERE A.publ_id=B.publ_id AND A.author_id!=B.author_id
GROUP BY A.author_id,B.author_id;

INSERT INTO graph
SELECT author_id_1, author_id_2, publications, 801 as FoR_id 
FROM coauthors.coauth 
WHERE author_id_1 in (SELECT id FROM author WHERE FoR_id = 801) 
AND author_id_2 in (SELECT id FROM author WHERE FoR_id = 801);


CREATE TEMPORARY TABLE temp AS
SELECT A.author_id as `author1`,B.author_id as `author2`,count(A.publ_id) as `publications`
FROM dblp.authors_publications as A, dblp.authors_publications as B
WHERE A.publ_id=B.publ_id AND A.author_id!=B.author_id
GROUP BY A.author_id,B.author_id;

INSERT INTO coauthors.coauth
SELECT distinct
case when author1 < author2 then author1 else author2 end as `author1`,
case when author1 > author2 then author1 else author2 end as `author2`,
publications
FROM temp;