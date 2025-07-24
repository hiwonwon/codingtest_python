-- 코드를 입력하세요
SELECT CATEGORY, sum(bs.sales) as 'TOTAL_SALES'
from book as b
join book_sales as bs
on b.book_id = bs.book_id
where bs.sales_date >='2022-01-01' and bs.sales_date<='2022-01-31'
group by category
order by category asc;