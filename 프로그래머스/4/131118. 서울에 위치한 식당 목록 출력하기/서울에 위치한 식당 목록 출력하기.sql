-- 코드를 입력하세요
with avg_score as (
    select rest_id, round(avg(review_score), 2) as SCORE
    from rest_review
    group by rest_id
)
select R.REST_ID, R.REST_NAME, R.FOOD_TYPE, R.FAVORITES, R.ADDRESS, A.SCORE
from rest_info R left join avg_score A
on R.rest_id = A.rest_id
where R.address like '서울%' and A.score is not null
order by A.score desc, R.favorites desc;