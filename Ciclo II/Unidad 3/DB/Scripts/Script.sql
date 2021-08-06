SELECT count() FROM sales s JOIN book b WHERE s.id_book = b.id AND b.isbn = 'fdsg8df89g7df987g'; 

SELECT isbn, title, year, amount FROM book b JOIN stock s ON b.id = s.id_book WHERE s.amount > 0;