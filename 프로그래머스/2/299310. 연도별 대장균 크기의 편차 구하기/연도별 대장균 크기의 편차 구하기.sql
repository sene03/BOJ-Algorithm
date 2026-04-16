with YEARLY_MAX as (
    select year(DIFFERENTIATION_DATE) as year, max(size_of_colony) as max_size from ECOLI_DATA group by year(DIFFERENTIATION_DATE)
)
select 
    year(E.DIFFERENTIATION_DATE) as YEAR, 
    (Y.max_size - E.SIZE_OF_COLONY) as YEAR_DEV,
    E.ID
from ECOLI_DATA E 
join YEARLY_MAX Y
on year(E.DIFFERENTIATION_DATE) = Y.year
order by YEAR, YEAR_DEV;