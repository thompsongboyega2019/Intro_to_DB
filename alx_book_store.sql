CREATE TABLE authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215)
);


CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(130),
    author_id INT,
    CONSTRAINT author_constraint
     FOREIGN KEY (author_id) REFERENCES authors(author_id),
    price DOUBLE,
    publication_date DATE
);


CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    CONSTRAINT customer_constraint
     FOREIGN KEY customer_id REFERENCES customers(customer_id)
);

CREATE TABLE orders_details (
    order_detail_id INT PRIMARY KEY,
    order_id INT,
    CONSTRAINT order_c
     FOREIGN KEY order_id REFERENCES orders(order_id),
    book_id INT,
    CONSTRAINT bk_id 
     FOREIGN KEY book_id REFERENCES books(book_id),
    quantity TEXT
);

