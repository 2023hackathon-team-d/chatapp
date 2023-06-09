import pymysql
from util.DB import DB

# データベースと接続し、ユーザの登録やユーザー情報を取得するクラス
class dbConnect:
    # ユーザー登録の関数
    def createUser(user):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO users (uid, user_name, email, password, mydream) VALUES (%s, %s, %s, %s, %s);"
            cur.execute(sql, (user.uid, user.name, user.email, user.password, ''))
            conn.commit()
        except Exception as e:
            print(e,'例外が発生しています')
            return None
        finally:
            cur.close()


    # ユーザー情報を得る関数
    def getUser(email):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM users WHERE email=%s;"
            cur.execute(sql, (email,))
            user = cur.fetchone()
            return user
        except Exception as e:
            print('例外' + str(e) + 'が発生しています')
            return None
        finally:
            cur.close()

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
            print(e,'例外が発生しています')
            return None
        finally:
            cur.close()

    # IDからチャンネル情報を得る関数 
    def getChannelById(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE id=%s;"
            cur.execute(sql, (cid,))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(e,'例外が発生しています')
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
            print(e,'例外が発生しています')
            return None
        finally:
            cur.close()

    #　チャンネルを加える関数 
    def addChannel(uid, newChannelName, newChannelDescription):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO channels (uid, channel_name, abstract) VALUES (%s, %s, %s);"
            cur.execute(sql, (uid, newChannelName, newChannelDescription))
            conn.commit()
        except Exception as e:
            print('例外' + str(e) + 'が発生しています')
            return None
        finally:
            cur.close()

    # チャンネル情報を取得する関数   
    def getChannelByName(channel_name):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE channel_name=%s;"
            cur.execute(sql, (channel_name))
            channel = cur.fetchone()
        except Exception as e:
            print('例外' + str(e) + 'が発生しました')
            return None
        finally:
            cur.close()
            return channel     

    #　チャンネルをアップデートする関数 
    def updateChannel(uid, newChannelName, newChannelDescription, cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "UPDATE channels SET uid=%s, channel_name=%s, abstract=%s WHERE id=%s;"
            cur.execute(sql, (uid, newChannelName, newChannelDescription, cid))
            conn.commit()
        except Exception as e:
            print('例外が' + str(e) + '発生しています')
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
            print('例外'+ str(e) +'が発生しています')
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
            print('例外'+ str(e) +'が発生しています')
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
            print('例外' + str(e) +'が発生しています')
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
            print('例外'+ str(e) +'が発生しています')
            return None
        finally:
            cur.close()

    def gettaskAll():
        try:
            conn = DB.getConnection() 
            cur = conn.cursor() 
            sql = "SELECT * FROM tasks;"
            cur.execute(sql) 
            tasks = cur.fetchall()
            return tasks
        except Exception as e:
            print(str(e)+ 'が発生しています')
            return None
        finally:
            cur.close()
    def gettaskById(uid):
        try:
            conn = DB.getConnection() 
            cur = conn.cursor() 
            sql = "SELECT * FROM tasks WHERE uid=%s;"
            cur.execute(sql, (uid)) 
            tasks = cur.fetchall() 
            return tasks
        except Exception as e:
            print(str(e)+ 'が発生しています')
            return None
        finally:
            cur.close()

    def gettaskByCId(cid):
            try:
                conn = DB.getConnection() 
                cur = conn.cursor() 
                sql = "SELECT * FROM tasks WHERE id=%s;"
                cur.execute(sql, (cid)) 
                task = cur.fetchone() 
                return task
            except Exception as e:
                print(str(e) + 'が発生しています')
                return None
            finally:
                cur.close()

    def task(uid, newtaskName, newtaskDescription):
            try:
                conn = DB.getConnection() 
                cur = conn.cursor() 
                sql = "INSERT INTO tasks (uid, task, limit_date) VALUES (%s, %s, %s);"
                cur.execute(sql, (uid, newtaskName, newtaskDescription)) 
                conn.commit() 
            except Exception as e:
                print(str(e)+ 'が発生しています')
                return None
            finally:
                cur.close()


    def gettaskByName(task_name): 
            try:
                conn = DB.getConnection()  
                cur = conn.cursor() 
                sql = "SELECT * FROM tasks WHERE name=%s;"
                cur.execute(sql, (task_name)) 
                task = cur.fetchone() 
            except Exception as e:
                print(str(e)+ 'が発生しました')
                return None
            finally:
                cur.close()


    def updatetask(uid, newtaskName, newtaskDescription, cid): 
            conn = DB.getConnection() 
            cur = conn.cursor() 
            sql = "UPDATE task SET uid=%s, name=%s, abstract=%s WHERE id=%s;"
            cur.execute(sql, (uid, newtaskName, newtaskDescription, cid)) 
            conn.commit() 
            cur.close()

    def deletetask(tid):
            try: 
                conn = DB.getConnection() 
                cur = conn.cursor() 
                sql = "DELETE FROM task WHERE id=%s;"
                cur.execute(sql, (tid)) 
                conn.commit() 
            except Exception as e:
                print(str(e) + 'が発生しています')
                return None
            finally:
                cur.close()

    def dream(mydream, uid):
            try:
                conn = DB.getConnection()
                cur = conn.cursor()
                sql = "UPDATE users SET mydream=%s WHERE uid=%s;"
                cur.execute(sql, (mydream, uid))
                conn.commit()
            except Exception as e:
                print(str(e)+ 'が発生しています')
                return None

            finally:
                cur.close()

    def getdream(uid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM users WHERE uid=%s;"
            cur.execute(sql, (uid,))
            users = cur.fetchone()
            return users
        except Exception as e:
            print('例外' + str(e) + 'が発生しています')
            return None
        finally:
            cur.close()            