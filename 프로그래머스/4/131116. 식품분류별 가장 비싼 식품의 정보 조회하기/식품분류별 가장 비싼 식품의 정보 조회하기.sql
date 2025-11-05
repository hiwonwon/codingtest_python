-- 코드를 입력하세요
SELECT CATEGORY, PRICE as "MAX_PRICE", PRODUCT_NAME
from FOOD_PRODUCT
where CATEGORY in ('과자', '국', '김치', '식용유') and 
price in (SELECT max(PRICE)
        from FOOD_PRODUCT
         group by CATEGORY)
order by price desc