-- 코드를 입력하세요
SELECT COUNT(distinct NAME) as count
From ANIMAL_INS
where Name IS NOT NULL;