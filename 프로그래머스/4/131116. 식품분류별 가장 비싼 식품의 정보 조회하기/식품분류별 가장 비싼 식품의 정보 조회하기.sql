SELECT CATEGORY, PRICE as MAX_PRICE, PRODUCT_NAME
from FOOD_PRODUCT
where PRICE in (
    select max(PRICE) as PRICE
    from FOOD_PRODUCT
    where CATEGORY in ('과자', '국', '김치', '식용유')
    group by CATEGORY)
and CATEGORY in ('과자', '국', '김치', '식용유')
order by MAX_PRICE desc;