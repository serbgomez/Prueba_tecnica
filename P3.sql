-- P3: Ventas del empleado 345 en 2022

-- Selección
SELECT 
	INITCAP(TO_CHAR(payment_date, 'Month')) as month, -- Extraer el mes del timestamp
	SUM(amount) as total
FROM 
	payment
	
-- Condiciones: empleado y año
WHERE 
	staff_id = 345 
	AND EXTRACT (YEAR FROM payment_date) = 2022

-- Agrupar y ordenar por meses
GROUP BY
	TO_CHAR(payment_date, 'Month')
ORDER BY
	MIN(EXTRACT(MONTH FROM payment_date));