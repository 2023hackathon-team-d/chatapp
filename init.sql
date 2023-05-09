#既存のchatappというデータベースとtestuserというユーザを削除
DROP DATABASE chatapp;
DROP USER 'testuser'@'localhost';

#chatappというデータベースとtestuserというユーザを作成
CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'testuser';
CREATE DATABASE chatapp;
USE chatapp　#chatappデータベースを使用宣言
GRANT ALL PRIVILEGES ON chatapp.* TO 'testuser'@'localhost';　#localhostで入ってきたユーザはデータベースへのすべてのアクセス権限あり

#usersテーブル作成
CREATE TABLE users (
    uid varchar(５０) PRIMARY KEY,
    user_name varchar(５０) UNIQUE NOT NULL,
    email varchar(５０) UNIQUE NOT NULL,
    #パスワードの最小文字数を8に設定する
　　　　　　　　SET GLOBAL validate_password.length=8,
    created_at TIMESTAMP,
    update_at TIMESTAMP,
);

#channelsテーブルを作成
CREATE TABLE channels (
    id serial PRIMARY KEY,
    uid varchar(50) REFERENCES users(uid),
    name varchar(50) UNIQUE NOT NULL,
    cate VARCHAR(50) UNIQUE NOT NULL,
    abstaract VARCHAR(50) NOT NULL,
);

＃messageテーブルを作成
CREATE TABLE messages (
    id serial PRIMARY KEY,
    uid varchar(50) REFERENCES users(uid),
    cid integer REFERENCES channels(id) ON DELETE CASCADE,
    message text,
    created_at timestamp not null default current_timestamp
);

#tasksテーブルを作成
CREATE TABLE tasks (
    id serial PRIMARY KEY,
    task varchar(50),
    limit datetime.starptime,
    create_at TIMESTAMP,
    update_at TIMESTAMP
);




