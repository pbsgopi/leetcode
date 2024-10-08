SELECT b.id
From Weather w
LEFT JOIN Weather b
on DATEDIFF(b.recordDate,w.recordDate)=1
where b.temperature>w.temperature