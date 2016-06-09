CREATE TABLE `dump` (
  `index` int(20) DEFAULT NULL,
  `uid` int(20) DEFAULT NULL,
  `time` int(20) DEFAULT NULL,
  `delete1` int(20) DEFAULT NULL,
  `delete2` int(20) DEFAULT NULL,
  `delete3` int(20) DEFAULT NULL,
  `delete4` int(20) DEFAULT NULL,
  `delete5` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


index,uid,time,delete1,delete2,delete3,delete4,delete5


1464613200 5/30/16 6AM
1464958800 6/3/16 6AM

1464839860

max 1465098316
min 1464613200
1465098316 - 1464839828

# all data
SELECT * FROM dump WHERE time BETWEEN 1464613200 AND 1464958800;

Day-by-day queries
SELECT * FROM dump WHERE time BETWEEN 1464613200 AND 1464699600;
SELECT * FROM dump WHERE time BETWEEN 1464699600 AND 1464786000;
SELECT * FROM dump WHERE time BETWEEN 1464786000 AND 1464872400;
SELECT * FROM dump WHERE time BETWEEN 1464872400 AND 1464958800;

SELECT avg(totalMorning1) AS avgn1 from classifications_multiday;
SELECT avg(totalMorning2) AS avgn2 from classifications_multiday;
SELECT avg(totalMorning3) AS avgn3 from classifications_multiday;
SELECT avg(totalMorning4) AS avgn4 from classifications_multiday;


avg total 10597.2872
night1 1082.1932
morn1 1419.6345
night2 1093.9426
morn2 1504.8564
night3 1198.4334
morn3 1553.5770
night4 1214.8851
morn4 1516.9191

SELECT * FROM dump WHERE id IN (1,2,3) AND time BETWEEN 1464872400 AND 1464958800;

# Series 1 
SELECT * FROM dump 
WHERE (time BETWEEN 1464613200 AND 1464699600)
AND `index` IN (SELECT `index` FROM classifications_multiday WHERE totalNight1 > 1082.1932);
SELECT * FROM dump 
WHERE (time BETWEEN 1464613200 AND 1464699600)
AND `index` IN (SELECT `index` FROM classifications_multiday WHERE totalMorning1 > 1419.6345);

# Series 2
SELECT * FROM dump 
WHERE (time BETWEEN 1464699600 AND 1464786000)
AND `index` IN (SELECT `index` FROM classifications_multiday WHERE totalNight2 > 1093.9426);
SELECT * FROM dump 
WHERE (time BETWEEN 1464699600 AND 1464786000)
AND `index` IN (SELECT `index` FROM classifications_multiday WHERE totalMorning2 > 1504.8564);

# Series 3
SELECT * FROM dump 
WHERE (time BETWEEN 1464786000 AND 1464872400)
AND `index` IN (SELECT `index` FROM classifications_multiday WHERE totalNight3 > 1198.4334);
SELECT * FROM dump 
WHERE (time BETWEEN 1464786000 AND 1464872400)
AND `index` IN (SELECT `index` FROM classifications_multiday WHERE totalMorning3 > 1553.5770);

# Series 4
SELECT * FROM dump 
WHERE (time BETWEEN 1464872400 AND 1464958800)
AND `index` IN (SELECT `index` FROM classifications_multiday WHERE totalNight4 > 1214.8851);
SELECT * FROM dump 
WHERE (time BETWEEN 1464872400 AND 1464958800)
AND `index` IN (SELECT `index` FROM classifications_multiday WHERE totalMorning4 > 1516.9191);