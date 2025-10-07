SELECT c.login, COUNT(o."inDelivery")
FROM "Orders" AS o JOIN "Couriers" AS c ON c.id=o."courierId"
WHERE o."inDelivery"='true'
GROUP BY c.login;