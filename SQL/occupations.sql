SELECT Doctor, Professor, Singer, Actor FROM (
    SELECT * FROM (
                    SELECT Name, Occupation, (
                        ROW_NUMBER() OVER (
                            PARTITION BY Occupation ORDER BY Name
                        )
                    ) AS row_num FROM OCCUPATIONS ORDER BY Name ASC
    ) 
    PIVOT ( MIN(Name) FOR Occupation IN (
        'Doctor' AS Doctor,
        'Professor' AS Professor,
        'Singer' AS Singer,
        'Actor' AS Actor)
    ) ORDER BY row_num
); 