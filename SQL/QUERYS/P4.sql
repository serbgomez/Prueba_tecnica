-- P4: Pago acumulado de cada cliente

/* Para identificar al cliente en la consulta he usado su número de cliente, pero se podría modificar fácilmente para
mostrar nombre y apellido en caso de que fuera necesario
*/

-- Selección
SELECT 
	customer_id,
	amount,
	/* Suma acumulada separada por clientes y ordenada por fecha (se asume que un mismo cliente no puede
	hacer dos compras de forma simultánea) */
	SUM(amount) OVER (PARTITION BY customer_id ORDER BY payment_date) AS cumulative_payment,
	DATE(payment_date) as payment_date
FROM 
	payment
-- Por facilidad de visionado, ordenar por cliente y fecha
ORDER BY 
	customer_id, payment_date;