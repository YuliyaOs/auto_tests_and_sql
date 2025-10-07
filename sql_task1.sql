Задание 1

SELECT c.login, COUNT(o."inDelivery")
FROM "Orders" AS o JOIN "Couriers" AS c ON c.id=o."courierId"
WHERE o."inDelivery"='true'
GROUP BY c.login;

Задание 2

SELECT track,
CASE 
WHEN "finished"='true' THEN '2'
WHEN "Orders".cancelled='true' THEN '-1'
WHEN "Orders"."inDelivery"='true' THEN '1'
ELSE '0'
END
FROM "Orders";