select d.id, d.department, count(e.id) as hired
from employee e 
join department d on (e.department_id = d.id)
where substr(e.datetime,1,4) = '2021' 
group by department
having hired > (select count(e.id)/12
                from employee e 
                where substr(e.datetime,1,4) = '2021'
            )
order by hired desc;



