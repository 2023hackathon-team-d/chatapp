-- 既存のchatappというデータベースとtestuserというユーザを削除
DROP DATABASE IF EXISTS chatapp;
DROP USER IF EXISTS 'testuser'@'localhost';

-- chatappというデータベースとtestuserというユーザを作成
CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'testuser';
CREATE DATABASE chatapp;
USE chatapp
GRANT ALL PRIVILEGES ON chatapp.* TO 'testuser'@'localhost';

-- usersテーブル作成
CREATE TABLE users (
    uid varchar(50) AUTO_INCREMENT PRIMARY KEY,
    user_name varchar(50) UNIQUE NOT NULL,
    email varchar(50) UNIQUE NOT NULL,
    password varchar(50) NOT NULL,
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- channelsテーブルを作成
CREATE TABLE channels (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uid varchar(50) REFERENCES users(uid),
    channel_name varchar(50) UNIQUE NOT NULL,
    cate VARCHAR(50) UNIQUE NOT NULL,
    abstract VARCHAR(50) NOT NULL
);

-- messageテーブルを作成
CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uid varchar(50) REFERENCES users(uid),
    cid integer REFERENCES channels(id) ON DELETE CASCADE,
    message text,
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- tasksテーブルを作成
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task varchar(50),
    limit_date datetime,
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);




