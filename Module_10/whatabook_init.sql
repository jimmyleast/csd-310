
   
/*
    Title: whatabook.init.sql
    Author: Jimmy Easter
    Date: 12/14/21
    Description: WhatABook database initialization script.
*/

-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('123456 N Walton Blvd, Bentonville, AR');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('Anna Karenina', 'Leo Tolstoy');

INSERT INTO book(book_name, author, details)
    VALUES('Madame Bovary', 'Gustave Flaubert', 'For daring to peer into the heart of an adulteress and enumerate its contents with profound dispassion, the author of Madame Bovary was tried for offenses against morality and religion');

INSERT INTO book(book_name, author, details)
    VALUES('War and Peace', 'Leo Tolstoy', "Epic in scale, War and Peace delineates in graphic detail events leading up to Napoleons invasion of Russia, and the impact of the Napoleonic era on Tsarist society, as seen through the eyes");

INSERT INTO book(book_name, author, details)
    VALUES('The Great Gatsby', 'F. Scott Fitzgerald', 'The novel chronicles an era that Fitzgerald himself dubbed the Jazz Age". Following the shock and chaos of World War I American society enjoyed unprecedented levels of prosperity during the "roar"');

INSERT INTO book(book_name, author, details)
    VALUES('Lolita', 'Vladimir Nabokov', 'The book is internationally famous for its innovative style and infamous for its controversial subject: the protagonist and unreliable narrator, middle aged Humbert Humbert, becomes obsessed');

INSERT INTO book(book_name, author, details)
    VALUES('Middlemarch', 'George Eliot', 'Middlemarch: A Study of Provincial Life is a novel by George Eliot, the pen name of Mary Anne Evans, later Marian Evans. It is her seventh novel, begun in 1869 and then put aside during the final');

INSERT INTO book(book_name, author, details)
    VALUES(' The Adventures of Huckleberry Finn', ' Mark Twain','Revered by all of the towns children and dreaded by all of its mothers, Huckleberry Finn is indisputably the most appealing child-hero in American literature. Unlike the tall-tale, idyllic world');

INSERT INTO book(book_name, author, details)
    VALUES('In Search of Lost Time', 'Marcel Proust','Swanns Way, the first part of A la recherche de temps perdu, Marcel Prousts seven-part cycle, was published in 1913. In it, Proust introduces the themes that run through the entire work');

INSERT INTO book(book_name, author, details)
    VALUES('The Stories of Anton Chekhov', 'Anton Chekhov','Anton Pavlovich Chekhov was a Russian short-story writer, playwright and physician, considered to be one of the greatest short-story writers in the history of world literature');

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Jimmy', 'Easter');

INSERT INTO user(first_name, last_name)
    VALUES('Traci', 'Easter');

INSERT INTO user(first_name, last_name)
    VALUES('Ashley', 'Easter');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Jimmy'), 
        (SELECT book_id FROM book WHERE book_name = 'War and Peace')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Traci'),
        (SELECT book_id FROM book WHERE book_name = 'Madame Bovary')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Ashley'),
        (SELECT book_id FROM book WHERE book_name = 'Lolita')
    );
