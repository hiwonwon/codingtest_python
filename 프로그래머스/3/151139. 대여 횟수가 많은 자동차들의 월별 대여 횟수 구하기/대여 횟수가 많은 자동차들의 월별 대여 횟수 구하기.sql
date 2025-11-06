-- 코드를 입력하세요
SELECT month(start_date) as MONTH, car_id, count(*) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where DATE_FORMAT(START_DATE,'%Y-%m') between '2022-08' and '2022-10' and car_id in(
        SELECT car_id
        from CAR_RENTAL_COMPANY_RENTAL_HISTORY
        where DATE_FORMAT(START_DATE,'%Y-%m') between '2022-08' and '2022-10'
        group by car_id
        having count(car_id)>=5)
group by car_id,month(start_date)
having Records >= 1
order by MONTH , car_id desc