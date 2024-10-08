# Write your MySQL query statement below
select product_name,year,price
from Sales S left join Product P
on P.Product_id=S.Product_id