-- 既存のchatappというデータベースとtestuserというユーザを削除
DROP DATABASE IF EXISTS chatapp;
DROP USER IF EXISTS 'testuser'@'localhost';

-- chatappというデータベースとtestuserというユーザを作成
CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'testuser';
CREATE DATABASE chatapp;
--chatappデータベースを使用宣言
USE chatapp
--localhostで入ってきたユーザはデータベースへのすべてのアクセス権限あり
GRANT ALL PRIVILEGES ON chatapp.* TO 'testuser'@'localhost';

-- usersテーブル作成
CREATE TABLE users (
    id AUTO_INCREMENT PRIMARY KEY
    user_name varchar(50) UNIQUE NOT NULL,
    email varchar(50) UNIQUE NOT NULL,
    password varchar(50) NOT NULL
    created_at TIMESTAMP,
    update_at TIMESTAMP,
    CONSTRAINT chk_password_length CHECK (length(password) >= 8)
);

-- channelsテーブルを作成
CREATE TABLE channels (
    id AUTO_INCREMENT PRIMARY KEY,
    uid varchar(50) REFERENCES users(uid),
    name varchar(50) UNIQUE NOT NULL,
    cate VARCHAR(50) UNIQUE NOT NULL,
    abstaract VARCHAR(50) NOT NULL
);

-- messageテーブルを作成
CREATE TABLE messages (
    id AUTO_INCREMENT PRIMARY KEY,
    uid varchar(50) REFERENCES users(uid),
    cid integer REFERENCES channels(id) ON DELETE CASCADE,
    message text,
    created_at timestamp not null default current_timestamp
);

-- tasksテーブルを作成
CREATE TABLE tasks (
    id AUTO_INCREMENT PRIMARY KEY,
    task varchar(50),
    limit_date datetime.starptime,
    create_at TIMESTAMP,
    update_at TIMESTAMP
);




