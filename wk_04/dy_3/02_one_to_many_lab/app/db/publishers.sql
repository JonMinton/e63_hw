DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255)
);

CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  genre VARCHAR(255),
  year_published INT,
  author_id INT NOT NULL REFERENCES authors(id) ON DELETE CASCADE
);


INSERT INTO 
  authors ("id", "first_name", "last_name") 
    VALUES(1, 'JK', 'Rowling');

-- INSERT INTO
--   books ("id", "title", "genre", "year_published", "author_id")
--     VALUES(1, "Harry Potter and the Philospher's Stone", "Fantasy", 1997, 1);


INSERT INTO 
  books ("id", "title", "genre", "year_published", "author_id") 
    VALUES(1, 'Harry Potter and the Philosopher''s Stone', 'Fantasy', 1997, 1);

INSERT INTO
  books ("id", "title", "genre", "year_published", "author_id")
    VALUES(2, 'Harry Potter and the Chamber of Secrets', 'Fantasy', 1998, 1);

INSERT INTO
  books ("id", "title", "genre", "year_published", "author_id")
    VALUES(3, 'Harry Potter and the Prisoner of Azkaban', 'Fantasy', 1999, 1);

INSERT INTO
  books ("id", "title", "genre", "year_published", "author_id")
    VALUES(4, 'Harry Potter and the Goblet of Fire', 'Fantasy', 2000, 1);

INSERT INTO
  books ("id", "title", "genre", "year_published", "author_id")
    VALUES(5, 'Harry Potter and the Order of the Phoenix', 'Fantasy', 2003, 1);

INSERT INTO
  books ("id", "title", "genre", "year_published", "author_id")
    VALUES(6, 'Harry Potter and the Half-Blood Prince', 'Fantasy', 2005, 1);

INSERT INTO
  books ("id", "title", "genre", "year_published", "author_id")
    VALUES(7, 'Harry Potter and the Deathly Hallows', 'Fantasy', 2007, 1);


INSERT INTO 
  authors ("id", "first_name", "last_name") 
    VALUES(2, 'JRR', 'Tolkien');

INSERT INTO
  books ("id", "title", "genre", "year_published", "author_id")
    VALUES(8, 'Sir Gawain & The Green Knight', 'Fantasy', 1925, 2);

INSERT INTO
  books ("id", "title", "genre", "year_published", "author_id")
    VALUES(9, 'The Hobbit: or There and Back Again', 'Fantasy', 1937, 2);

INSERT INTO
  books ("id", "title", "genre", "year_published", "author_id")
    VALUES(10, 'Farmer Giles of Ham', 'Fantasy', 1949, 2);

INSERT INTO
  books ("id", "title", "genre", "year_published", "author_id")
    VALUES(11, 'The Fellowship of the Ring: being the first part of The Lord of the Rings', 'Fantasy', 1954, 2);

INSERT INTO
  books ("id", "title", "genre", "year_published", "author_id")
    VALUES(12, 'The Two Towers: being the second part of The Lord of the Rings', 'Fantasy', 1954, 2);

INSERT INTO
  books ("id", "title", "genre", "year_published", "author_id")
    VALUES(13, 'The Return of the King: being the third part of The Lord of the Rings', 'Fantasy', 1955, 2);


INSERT INTO 
  authors ("id", "first_name", "last_name") 
    VALUES(3, 'George R R ', 'Martin');  

INSERT INTO 
  authors ("id", "first_name", "last_name") 
    VALUES(4, 'AC', 'Grayling');

INSERT INTO 
  authors ("id", "first_name", "last_name") 
    VALUES(5, 'Steven', 'Pinker');

INSERT INTO  
  authors ("id", "first_name", "last_name") 
    VALUES(6, 'Steven', 'Rose');

INSERT INTO 
  authors ("id", "first_name", "last_name") 
    VALUES(7, 'David', 'Graeber');

