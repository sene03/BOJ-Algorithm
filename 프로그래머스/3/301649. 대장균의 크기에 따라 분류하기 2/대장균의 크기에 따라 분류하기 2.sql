with E as (
    select ID, percent_rank() over (order by SIZE_OF_COLONY desc) as per
    from ECOLI_DATA
)
select ID, 
    (case 
        when per <= 0.25 then 'CRITICAL'
        when per <= 0.50 then 'HIGH'
        when per <= 0.75 then 'MEDIUM'
        else 'LOW'
    end) as COLONY_NAME
from E
order by ID asc;