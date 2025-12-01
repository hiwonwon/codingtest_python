-- 코드를 작성해주세요
#퍼센트를 미리 두고 case when?
select id,
    case when a.percent <= 0.25 then "CRITICAL"
        when  a.percent<= 0.5 then "HIGH"
        when  a.percent<= 0.75 then "MEDIUM"
        else "LOW"
        end as COLONY_NAME
from (
    select id,
    percent_rank() over (order by SIZE_OF_COLONY desc) as 'percent'
    from ECOLI_DATA
    ) as a
order by id