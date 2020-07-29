/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT CONCAT(CONCAT(CONCAT(NAME, '('), SUBSTR(OCCUPATION, 1, 1)), ')') AS Name
FROM OCCUPATIONS
ORDER BY NAME;

SELECT CONCAT(CONCAT(CONCAT(CONCAT('There are a total of ', COUNT(OCCUPATION)), ' '), LOWER(OCCUPATION)), 's.') AS STATEMENT
FROM OCCUPATIONS
GROUP BY OCCUPATION
ORDER BY STATEMENT;