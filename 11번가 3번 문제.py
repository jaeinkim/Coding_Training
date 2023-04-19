-- 기대 테이블 주의 요건
--    1) all_test_cases = test_cases 테이블에서 group_name 별로 카운트한 것
--    2) passed_test_cases = test_cases 테이블에서 status가 OK인 것만 필터링하여 카운트한 것
--    3) total_values = 본 테이블의 passed_test_cases * test_groups 테이블의 동일 name의 test_value
                                                                                                                                                                                                                   --    4) total_value 내림차순 및 같은 경우 name 오름차순

select   A1.name                                                                as name
,sum(case when A2.id is not null then 1 else 0 end)                     as all_test_cases
,sum(case when A2.status = 'OK' then 1 else 0 end)                      as passed_test_cases
,sum(case when A2.status = 'OK' then 1 else 0 end) * max(A1.test_value) as total_value
from        test_groups     A1
left join   test_cases      A2
on          A1.name = A2.group_name
group by    name
order by    total_value desc, name