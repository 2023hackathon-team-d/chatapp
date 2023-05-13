from flask import Flask, request, redirect, render_template, session, flash
from models import dbConnect
from util.user import User
from datetime import timedelta
import hashlib
import uuid
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # セッションで使用する秘密鍵を設定します
app.permanent_session_lifetime = timedelta(days=30)


@app.route('/signup')
def signup():
    return render_template('registration/signup.html')

# ユーザ登録
@app.route('/signup', methods=['GET','POST'])
def userSignup():
    name = request.form.get('name')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if name == '' or email =='' or password1 == '' or password2 == '':
        flash('空のフォームがあるようです')
    elif password1 != password2:
        flash('二つのパスワードの値が違っています')
    elif re.match(pattern, email) is None:
        flash('正しいメールアドレスの形式ではありません')
    else:
        uid = uuid.uuid4()
        password = hashlib.sha256(password1.encode('utf-8')).hexdigest()
        user = User(uid, name, email, password)
        DBuser = dbConnect.getUser(email)

        if DBuser != None:
            flash('既に登録されているようです')
        else:
            dbConnect.createUser(user)
            UserId = str(uid)
            session['uid'] = UserId
            return redirect('/')
    return redirect('/signup')

@app.route('/login')
def login():
    return render_template('registration/login.html')

# ログイン
@app.route('/login', methods=['POST'])
def userLogin():
    email = request.form.get('email')
    password = request.form.get('password')
    
    if email =='' or password == '':
        flash('空のフォームがあるようです')
    else:
        user = dbConnect.getUser(email)
        if user is None:
            flash('このユーザーは存在しません')
        else:
            hashPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
            if hashPassword != user["password"]:
                flash('パスワードが間違っています！')
            else:
                session['uid'] = user["uid"]
                return redirect('/mypage')
    return redirect('/login')

#ログアウト
@app.route('/logout')
def logout():
    session.clear()  # セッションからユーザーIDを削除します
    return redirect('/login')

#マイページ
@app.route('/mypage')
def mypage():
    uid = session.get('uid')
    channels = dbConnect.getChannelAll()
    if uid is None:
        return redirect('/login')
    return render_template('mypage.html', uid=uid, channels = channels )
           
#チャットリスト
@app.route('/')
def index():
    uid = session.get("uid")
    if uid is None:
         return redirect('/login')
    else:
         channels = dbConnect.getChannelAll()
         cid = request.form.get('cid')
         channel = dbConnect.getChannelById(cid)
         return render_template('index.html', channels=channels, uid=uid, channel=channel)

# チャンネル追加
@app.route('/', methods=['GET','POST'])
def add_channel():
    uid = session.get('uid')
    if uid is None:
        return redirect('/login')
    channel_name = request.form.get('channel-title')
    channel = dbConnect.getChannelByName(channel_name)
    if channel == None:
        channel_description = request.form.get('channel-description')
        dbConnect.addChannel(uid, channel_name, channel_description)
        return redirect('/')
    else:
        error = '既に同じチャンネルが存在しています'
        return render_template('error/error.html', error_message=error)
    
# チャンネル編集
@app.route('/update_channel', methods=['GET','POST'])
def update_channel():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')

    cid = request.form.get('cid')
    channel_name = request.form.get('channel-title')
    channel_description = request.form.get('channel-description')

    dbConnect.updateChannel(channel_name, channel_description, cid)
    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)
    return render_template('detail.html', messages=messages, channel=channel, uid=uid)


# チャンネル削除
@app.route('/delete/<cid>')
def delete_channel(cid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    else:
        channel = dbConnect.getChannelById(cid)
        if channel["uid"] != uid:
            flash('チャンネルは作成者のみ削除可能です')
            return redirect ('/')
        else:
            dbConnect.deleteChannel(cid)
            channels = dbConnect.getChannelAll()
            return render_template('index.html', channels=channels, uid=uid)

# チャットの中身
# uidもmessageと一緒に返す
@app.route('/detail/<cid>')
def detail(cid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    cid = cid
    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)
    task = dbConnect.get
    return render_template('detail.html', messages=messages, channel=channel, uid=uid task=task)

#メッセージ投稿
@app.route('/message', methods=['GET','POST'])
def add_message():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')

    message = request.form.get('message')
    channel_id = request.form.get('channel_id')

    if message:
        dbConnect.createMessage(uid, channel_id, message)

    channel = dbConnect.getChannelById(channel_id)
    messages = dbConnect.getMessageAll(channel_id)

    return render_template('detail.html', messages=messages, channel=channel, uid=uid)

# メッセージ削除
@app.route('/delete_message', methods=['GET','POST'])
def delete_message():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')

    message_id = request.form.get('message_id')
    cid = request.form.get('channel_id')
    if message_id:
        dbConnect.deleteMessage(message_id)

    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)

    return render_template('detail.html', messages=messages, channel=channel, uid=uid)

# TODOLIST
@app.route('/todolist', methods=['GET', 'POST'])
def todolist():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    else:
        return render_template('todolist.html', uid=uid)
    
# taskを作成
@app.route('/add-task', methods=['GET','POST'])
def add_task():
    uid = session.get('uid')
    if uid is None:
        return redirect('/login')
    title = request.form.get('title')
    if title:
        add_task_title = request.form.get('add_task_title')
        dbConnect.addTask(uid, add_task_title)
    return redirect('/')

# taskを編集
@app.route('/update-task', methods=['GET','POST'])
def update_task():
    uid = session.get('uid')
    if uid is None:
         return redirect('/login')
    title = request.form.get('title')
    if title:
         update_task_title = request.form.get('update_task_title')
         dbConnect.updateTask(uid,title)
    return redirect('/')

# taskを削除
@app.route('/delete-task/<tid>', methods=['GET','POST'])
def delete_ask(tid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    else: 
        task = dbConnect.getChannelById(tid)
    if task:
        dbConnect.deleteTask(uid, tid)
    return redirect('/')

#HTTPレスポンスエラー
@app.errorhandler(404)
def show_error404(error):
    return render_template('error/404.html')

@app.errorhandler(500)
def show_error500(error):
    return render_template('error/500.html')



if __name__ == '__main__':
    app.run(debug=True)



