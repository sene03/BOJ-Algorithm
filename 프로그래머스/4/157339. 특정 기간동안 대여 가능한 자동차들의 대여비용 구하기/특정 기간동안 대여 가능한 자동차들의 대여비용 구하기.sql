with RES as (
    select C.CAR_ID, C.CAR_TYPE, 
    C.DAILY_FEE*(1-D.DISCOUNT_RATE/100)*30
       as FEE
from 
-- 대여가능한 car id
(
    select CAR_ID, CAR_TYPE, DAILY_FEE
    from CAR_RENTAL_COMPANY_CAR
    where CAR_ID not in (
        select CAR_ID from CAR_RENTAL_COMPANY_RENTAL_HISTORY
	where END_DATE >= '2022-11-01' and START_DATE <= '2022-11-30'
        )
    and CAR_TYPE in ('SUV', '세단')
) C
left join 
-- discount rate
(
    select CAR_TYPE, DISCOUNT_RATE
    from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    where CAR_TYPE in ('SUV', '세단')
    and DURATION_TYPE = '30일 이상'
) D
on C.CAR_TYPE = D.CAR_TYPE
)
select * from RES
where FEE >= 500000 and FEE < 2000000
order by FEE desc, CAR_TYPE asc, CAR_ID desc;