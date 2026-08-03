select b.CATEGORY, sum(s.SALES) as TOTAL_SALES
from BOOK_SALES s 
join BOOK b on s.BOOK_ID = b.BOOK_ID
where s.SALES_DATE between '2022-01-01' and '2022-01-31'
group by b.CATEGORY
order by b.CATEGORY;
