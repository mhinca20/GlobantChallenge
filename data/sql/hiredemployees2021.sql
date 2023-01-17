select department, job 
        ,count(case when substr(e.datetime,6,2) in ('01','02','03') then e.id end) as Q1
        ,count(case when substr(e.datetime,6,2) in ('04','05','06') then e.id end) as Q2
        ,count(case when substr(e.datetime,6,2) in ('07','08','09') then e.id end) as Q3
        ,count(case when substr(e.datetime,6,2) in ('10','11','12') then e.id end) as Q4
from
employee e 
join job j on (e.job_id = j.id)
join department d on (e.department_id = d.id)
where substr(e.datetime,1,4) = '2021'
group by job, department
order by department, job;