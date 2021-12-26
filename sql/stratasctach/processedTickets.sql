select type,
    (CAST(SUM(CASE WHEN processed = True THEN 1 ELSE 0 END) AS float) / COUNT(*))
from facebook_complaints
GROUP BY type

--theirs
SELECT
 type,
 SUM(CASE WHEN processed THEN 1 ELSE 0 END) :: NUMERIC /
 COUNT(*) AS processed_rate
FROM
 facebook_complaints
GROUP BY
 type
 
 --discussions
 select type, 
avg(CASE WHEN processed = 'TRUE' then 1 else 0 END) as prate  
from facebook_complaints
group by type;
