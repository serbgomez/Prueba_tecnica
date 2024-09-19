-- P5: Conteo de películas por categoría e idioma

-- Selección, con la correspondiente agrupación de tablas
SELECT 
	c.name as category, 
	l.name as language, 
	SUM(f.film_id) as NumFilms
FROM 	
	film_category fc
JOIN
	film f ON f.film_id = fc.film_id
JOIN 
	language l ON l.language_id = f.language_id
JOIN
	category c ON c.category_id = fc.category_id

-- Agrupar por categoría e idioma
GROUP BY
	c.name, l.name;
	
/* 
En respuesta a la pregunta, la propia estructura de la base de datos, en concreto la tabla "Film_category",
indica que la relación entre películas y categoríases many to many, es decir, que una misma película puede pertencer 
a varias categorías (y evidentemente hay varias películas de cada categoría). Por lo tanto, una película
que sea de varias categorías se estaría contando múltiples veces en este recuento, y la suma de la columna NumFilms
será siempre mayor que el número total de películas en el sistema
*/