-- P2: Clientes que no han hecho ninguna compra

-- Selección
SELECT 
	customer.first_name, 
	customer.last_name
FROM 
	customer
LEFT JOIN 
	payment ON customer.customer_id = payment.customer_id
-- Condición: no aparecen en la tabla "payment"
WHERE 
	payment.customer_id IS NULL;