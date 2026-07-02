select ID from ECOLI_DATA
where PARENT_ID in (
-- 2세대 ID 추출
select a.ID
from ECOLI_DATA a
join ECOLI_DATA b on a.PARENT_ID = b.ID
where b.PARENT_ID is NULL
    )
order by ID;
    
