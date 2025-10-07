SELECT track,
CASE 
WHEN "finished"='true' THEN '2'
WHEN "Orders".cancelled='true' THEN '-1'
WHEN "Orders"."inDelivery"='true' THEN '1'
ELSE '0'
END
FROM "Orders";