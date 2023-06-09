DROP DATABASE chatapp;
DROP USER 'user'@'localhost';

CREATE USER 'user'@'localhost' IDENTIFIED BY 'testuser';
CREATE DATABASE chatapp;

USE chatapp
GRANT ALL PRIVILEGES ON chatapp.* TO 'user'@'localhost';

CREATE TABLE users (
    uid varchar(50) PRIMARY KEY,
    user_name varchar(50) UNIQUE NOT NULL,
    email varchar(50) UNIQUE NOT NULL,
    password varchar(255) NOT NULL,
    mydream varchar(50) NULL,
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE channels (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uid varchar(50) REFERENCES users(uid),
    channel_name varchar(50) UNIQUE NOT NULL,
    abstract VARCHAR(50) NOT NULL
);

-- messageテーブルを作成
CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uid varchar(50) REFERENCES users(uid),
    cid integer REFERENCES channels(id) ON DELETE CASCADE,
    message text,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uid varchar(50) REFERENCES users(uid),
    task varchar(50),
    limit_date datetime,
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
