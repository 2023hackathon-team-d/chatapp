--既存のchatappというデータベースとtestuserというユーザを削除
DROP DATABASE chatapp;
DROP USER 'testuser'@'localhost';

--chatappというデータベースとtestuserというユーザを作成
CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'testuser';
CREATE DATABASE chatapp;
USE chatapp　#chatappデータベースを使用宣言
GRANT ALL PRIVILEGES ON chatapp.* TO 'testuser'@'localhost';　#localhostで入ってきたユーザはデータベースへのすべてのアクセス権限あり

--usersテーブル作成
CREATE TABLE users (
    uid varchar(５０) PRIMARY KEY,
    user_name varchar(５０) UNIQUE NOT NULL,
    email varchar(５０) UNIQUE NOT NULL,
    password varchar(50) NOT NULL
    created_at TIMESTAMP,
    update_at TIMESTAMP,
    CONSTRAINT chk_password_length CHECK (length(password) >= 8)
);

--channelsテーブルを作成
CREATE TABLE channels (
    id AUTO_INCREMENT PRIMARY KEY,
    uid varchar(50) REFERENCES users(uid),
    name varchar(50) UNIQUE NOT NULL,
    cate VARCHAR(50) UNIQUE NOT NULL,
    abstaract VARCHAR(50) NOT NULL,
);

--messageテーブルを作成
CREATE TABLE messages (
    id AUTO_INCREMENT PRIMARY KEY,
    uid varchar(50) REFERENCES users(uid),
    cid integer REFERENCES channels(id) ON DELETE CASCADE,
    message text,
    created_at timestamp not null default current_timestamp
);

--tasksテーブルを作成
CREATE TABLE tasks (
    id AUTO_INCREMENT PRIMARY KEY,
    task varchar(50),
    limit datetime.starptime,
    create_at TIMESTAMP,
    update_at TIMESTAMP
);




