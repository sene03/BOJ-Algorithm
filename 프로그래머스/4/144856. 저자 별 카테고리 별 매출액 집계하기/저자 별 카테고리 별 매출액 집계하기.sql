with s as 
(
    select BOOK_ID, SUM(SALES) as SUM_SALES
    from BOOK_SALES 
    where SALES_DATE between '2022-01-01' and '2022-01-31'
    group by BOOK_ID
    order by BOOK_ID
)

select a.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY, sum(b.PRICE*s.SUM_SALES) as TOTAL_SALES
from s 
join BOOK b on s.BOOK_ID = b.BOOK_ID
join AUTHOR a on b.AUTHOR_ID = a.AUTHOR_ID
group by b.AUTHOR_ID, b.CATEGORY
order by a.AUTHOR_ID asc, CATEGORY desc;
