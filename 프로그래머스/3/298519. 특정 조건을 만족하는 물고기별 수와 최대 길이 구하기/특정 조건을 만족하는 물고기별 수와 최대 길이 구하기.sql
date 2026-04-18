with A as (
    select 
        FISH_TYPE, 
        count(*) as FISH_COUNT,
        avg(IFNULL(LENGTH, 10)) as AVG_LENGTH,
        max(IFNULL(LENGTH,10)) as MAX_LENGTH
    from FISH_INFO
    group by FISH_TYPE
)
select FISH_COUNT, MAX_LENGTH, FISH_TYPE
from A
where AVG_LENGTH >= 33
order by FISH_TYPE;