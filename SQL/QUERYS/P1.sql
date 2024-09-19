-- Pregunta 1: Lista de clientes que se han gastado más de 100€

-- Seleccionar columnas
SELECT 
	customer.first_name, 
	customer.last_name, 
	SUM(payment.amount)
FROM 
	customer
JOIN 
	payment ON payment.customer_id = customer.customer_id
-- Agrupar por clientes
GROUP BY 
	customer.customer_id
-- Condición de filtrado (Gasto total)
HAVING 
	SUM(payment.amount) > 100;