SHOW DATABASES;

CREATE DATABASE company;

COMMIT;

USE company;

-- board 테이블 생성
CREATE TABLE board (
    no INT AUTO_INCREMENT PRIMARY KEY,      -- 글번호, 자동 증가
    title VARCHAR(255) NOT NULL,            -- 글제목
    content TEXT NOT NULL,                  -- 글내용
    author VARCHAR(100) NOT NULL,           -- 작성자
    resdate DATETIME DEFAULT CURRENT_TIMESTAMP,  -- 작성일, 기본값 현재 날짜/시간
    hits INT DEFAULT 0                      -- 조회수, 기본값 0
);

-- member 테이블 생성
CREATE TABLE member (
    id VARCHAR(50) PRIMARY KEY,             -- 아이디
    pw VARCHAR(255) NOT NULL,               -- 비밀번호
    name VARCHAR(100) NOT NULL,             -- 회원명
    birth DATE NOT NULL,                    -- 생년월일
    email VARCHAR(255) NOT NULL,            -- 이메일
    tel VARCHAR(20),                        -- 연락처
    addr1 VARCHAR(255),                     -- 기본 주소
    addr2 VARCHAR(255),                     -- 상세 주소
    postcode VARCHAR(10),                   -- 우편번호
    regdate DATETIME DEFAULT CURRENT_TIMESTAMP  -- 가입일, 기본값 현재 날짜/시간
);


CREATE TABLE qna (
    qno INT AUTO_INCREMENT PRIMARY KEY,
    lev INT DEFAULT 0,
    parno INT,
    title VARCHAR(255),
    content TEXT,
    author VARCHAR(255),
    resdate DATETIME DEFAULT CURRENT_TIMESTAMP,
    hits INT DEFAULT 0
);


CREATE TABLE dataroom (
    dno INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    content TEXT,
    author VARCHAR(255),
    datafile VARCHAR(255),
    resdate DATETIME DEFAULT CURRENT_TIMESTAMP,
    hits INT DEFAULT 0
);


CREATE TABLE product (
    pno INT AUTO_INCREMENT PRIMARY KEY,
    cate VARCHAR(255),
    pname VARCHAR(255),
    pcontent TEXT,
    img1 VARCHAR(255),
    img2 VARCHAR(255),
    img3 VARCHAR(255),
    resdate DATETIME DEFAULT CURRENT_TIMESTAMP,
    hits INT DEFAULT 0
);

COMMIT;

SHOW TABLES;

-- board 테이블에 대한 더미 데이터 삽입
INSERT INTO board (title, content, author) VALUES
('First Post', 'This is the first post.', 'Alice'),
('Second Post', 'This is the second post.', 'Bob'),
('Third Post', 'This is the third post.', 'Charlie'),
('Fourth Post', 'This is the fourth post.', 'David'),
('Fifth Post', 'This is the fifth post.', 'Eve'),
('Sixth Post', 'This is the sixth post.', 'Frank'),
('Seventh Post', 'This is the seventh post.', 'Grace'),
('Eighth Post', 'This is the eighth post.', 'Heidi'),
('Ninth Post', 'This is the ninth post.', 'Ivan'),
('Tenth Post', 'This is the tenth post.', 'Judy'),
('Eleventh Post', 'This is the eleventh post.', 'Mallory');

-- member 테이블에 대한 더미 데이터 삽입
INSERT INTO member (id, pw, name, birth, email, tel, addr1, addr2, postcode) VALUES
('alice', 'password1', 'Alice', '1990-01-01', 'alice@example.com', '010-1234-5678', '123 Main St', 'Apt 101', '12345'),
('bob', 'password2', 'Bob', '1991-02-02', 'bob@example.com', '010-2345-6789', '234 Elm St', 'Apt 202', '23456'),
('charlie', 'password3', 'Charlie', '1992-03-03', 'charlie@example.com', '010-3456-7890', '345 Oak St', 'Apt 303', '34567'),
('david', 'password4', 'David', '1993-04-04', 'david@example.com', '010-4567-8901', '456 Pine St', 'Apt 404', '45678'),
('eve', 'password5', 'Eve', '1994-05-05', 'eve@example.com', '010-5678-9012', '567 Maple St', 'Apt 505', '56789'),
('frank', 'password6', 'Frank', '1995-06-06', 'frank@example.com', '010-6789-0123', '678 Cedar St', 'Apt 606', '67890'),
('grace', 'password7', 'Grace', '1996-07-07', 'grace@example.com', '010-7890-1234', '789 Birch St', 'Apt 707', '78901'),
('heidi', 'password8', 'Heidi', '1997-08-08', 'heidi@example.com', '010-8901-2345', '890 Walnut St', 'Apt 808', '89012'),
('ivan', 'password9', 'Ivan', '1998-09-09', 'ivan@example.com', '010-9012-3456', '901 Chestnut St', 'Apt 909', '90123'),
('judy', 'password10', 'Judy', '1999-10-10', 'judy@example.com', '010-0123-4567', '012 Spruce St', 'Apt 1010', '01234'),
('mallory', 'password11', 'Mallory', '2000-11-11', 'mallory@example.com', '010-1234-5678', '123 Ash St', 'Apt 1111', '12345');

-- qna 테이블에 대한 더미 데이터 삽입
INSERT INTO qna (lev, parno, title, content, author) VALUES
(0, NULL, 'Question 1', 'This is the first question.', 'Alice'),
(0, NULL, 'Question 2', 'This is the second question.', 'Bob'),
(0, NULL, 'Question 3', 'This is the third question.', 'Charlie'),
(0, NULL, 'Question 4', 'This is the fourth question.', 'David'),
(0, NULL, 'Question 5', 'This is the fifth question.', 'Eve'),
(0, NULL, 'Question 6', 'This is the sixth question.', 'Frank'),
(0, NULL, 'Question 7', 'This is the seventh question.', 'Grace'),
(0, NULL, 'Question 8', 'This is the eighth question.', 'Heidi'),
(0, NULL, 'Question 9', 'This is the ninth question.', 'Ivan'),
(0, NULL, 'Question 10', 'This is the tenth question.', 'Judy'),
(0, NULL, 'Question 11', 'This is the eleventh question.', 'Mallory');

-- dataroom 테이블에 대한 더미 데이터 삽입
INSERT INTO dataroom (title, content, author, datafile) VALUES
('Data 1', 'This is the first data.', 'Alice', 'file1.pdf'),
('Data 2', 'This is the second data.', 'Bob', 'file2.pdf'),
('Data 3', 'This is the third data.', 'Charlie', 'file3.pdf'),
('Data 4', 'This is the fourth data.', 'David', 'file4.pdf'),
('Data 5', 'This is the fifth data.', 'Eve', 'file5.pdf'),
('Data 6', 'This is the sixth data.', 'Frank', 'file6.pdf'),
('Data 7', 'This is the seventh data.', 'Grace', 'file7.pdf'),
('Data 8', 'This is the eighth data.', 'Heidi', 'file8.pdf'),
('Data 9', 'This is the ninth data.', 'Ivan', 'file9.pdf'),
('Data 10', 'This is the tenth data.', 'Judy', 'file10.pdf'),
('Data 11', 'This is the eleventh data.', 'Mallory', 'file11.pdf');

-- product 테이블에 대한 더미 데이터 삽입
INSERT INTO product (cate, pname, pcontent, img1, img2, img3) VALUES
('Category 1', 'Product 1', 'This is the first product.', 'img1a.jpg', 'img1b.jpg', 'img1c.jpg'),
('Category 2', 'Product 2', 'This is the second product.', 'img2a.jpg', 'img2b.jpg', 'img2c.jpg'),
('Category 3', 'Product 3', 'This is the third product.', 'img3a.jpg', 'img3b.jpg', 'img3c.jpg'),
('Category 4', 'Product 4', 'This is the fourth product.', 'img4a.jpg', 'img4b.jpg', 'img4c.jpg'),
('Category 5', 'Product 5', 'This is the fifth product.', 'img5a.jpg', 'img5b.jpg', 'img5c.jpg'),
('Category 6', 'Product 6', 'This is the sixth product.', 'img6a.jpg', 'img6b.jpg', 'img6c.jpg'),
('Category 7', 'Product 7', 'This is the seventh product.', 'img7a.jpg', 'img7b.jpg', 'img7c.jpg'),
('Category 8', 'Product 8', 'This is the eighth product.', 'img8a.jpg', 'img8b.jpg', 'img8c.jpg'),
('Category 9', 'Product 9', 'This is the ninth product.', 'img9a.jpg', 'img9b.jpg', 'img9c.jpg'),
('Category 10', 'Product 10', 'This is the tenth product.', 'img10a.jpg', 'img10b.jpg', 'img10c.jpg'),
('Category 11', 'Product 11', 'This is the eleventh product.', 'img11a.jpg', 'img11b.jpg', 'img11c.jpg');



SELECT * FROM board;

SELECT * FROM product;
