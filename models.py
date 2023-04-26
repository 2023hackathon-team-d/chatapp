import pymysql
from DB import DB

# データベースと接続し、ユーザの登録やユーザー情報を取得するクラス
class dbConnect:
    # ユーザー登録の関数
    def createUser(user):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO users (uid, user_name, email, password) VALUES (%s, %s, %s, %s);"
            cur.execute(sql, (user.uid, user.name, user.email, user.password))
            conn.commit()
        except Exception as e:
            print('例外が発生しています')
            return None
        finally:
            cur.close()


    # ユーザー情報を得る関数
    def getUser(email):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM users WHERE email=%s;"
            cur.execute(sql, (email))
            user = cur.fetchone()
            return user
        except Exception as e:
            print('例外' + e + 'が発生しています')
            return None
        finally:
            cur.close

    # チャンネル情報を得る関数
    def getChannelAll():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels;"
            cur.execute(sql)
            channels = cur.fetchall()
            return channels
        except Exception as e:
            print('例外が発生しています')
            return None
        finally:
            cur.close()

    # IDからチャンネル情報を得る関数 
    def getChannelById(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE id=%s;"
            cur.execute(sql, (cid))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print('例外が発生しています')
            return None
        finally:
            cur.close()

    # チャンネル名からチャンネル情報を得る関数
    def getChannelByName(channel_name):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE name=%s;"
            cur.execute(sql, (channel_name))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print('例外が発生しています')
            return None
        finally:
            cur.close()

    #　チャンネルを加える関数 
    def addChannel(uid, newChannelName):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO channels (uid, name) VALUES (%s, %s);"
            cur.execute(sql, (uid, newChannelName))
            conn.commit()
        except Exception as e:
            print('例外' + e + 'が発生しています')
            return None
        finally:
            cur.close()

    # チャンネル情報を取得する関数   
    def getChannelByName(channel_name):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE name=%s;"
            cur.execute(sql, (channel_name))
            channel = cur.fetchone()
        except Exception as e:
            print('例外' + e + 'が発生しました')
            return None
        finally:
            cur.close()
            return channel     

    #　チャンネルをアップデートする関数 
    def updateChannel(uid, newChannelName, cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "UPDATE channels SET uid=%s, name=%s, WHERE id=%s;"
            cur.execute(sql, (uid, newChannelName, cid))
            conn.commit()
        except Exception as e:
            print('例外が' + e + '発生しています')
            return None
        finally:    
            cur.close()

    #チャンネルを消去する関数
    def deleteChannel(cid):
        try: 
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM channels WHERE id=%s;"
            cur.execute(sql, (cid))
            conn.commit()
        except Exception as e:
            print('例外'+ e +'が発生しています')
            return None
        finally:
            cur.close()

    # メッセージを呼び出す関数 
    def getMessageAll(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT id,u.uid, user_name, message FROM messages AS m INNER JOIN users AS u ON m.uid = u.uid WHERE cid = %s;"
            cur.execute(sql, (cid))
            messages = cur.fetchall()
            return messages
        except Exception as e:
            print('例外'+ e +'が発生しています')
            return None
        finally:
            cur.close()

    # メッセージを加える関数 
    def createMessage(uid, cid, message):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO messages(uid, cid, message) VALUES(%s, %s, %s)"
            cur.execute(sql, (uid, cid, message))
            conn.commit()
        except Exception as e:
            print('例外' + e +'が発生しています')
            return None
        finally:
            cur.close()

    # メッセージを消去する関数 
    def deleteMessage(message_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM messages WHERE id=%s;"
            cur.execute(sql, (message_id))
            conn.commit()
        except Exception as e:
            print('例外'+ e +'が発生しています')
            return None
        finally:
            cur.close()