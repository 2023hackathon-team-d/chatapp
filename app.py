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

@app.route('/signup', methods=['POST'])　#ユーザ登録
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

@app.route('/login', methods=['POST'])　#ログイン
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
                return redirect('/')
    return redirect('/login.html')

@app.route('/logout')　#ログアウト
def logout():
    session.clear()  # セッションからユーザーIDを削除します
    return redirect('/login.html')

@app.route('/')　#チャットリスト
def index():
    if 'user_id' not in session:  # ユーザーが認証されていない場合はログインページにリダイレクトします
        return redirect('/login')
    user_id = session['user_id']
    user = dbConnect.get_user(user_id)  # ログイン中のユーザーを取得します
    return render_template('index.html', user=user)

@app.route('/mypage')　　#マイページ
def mypage():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    return render_template('/mypage.html')

@app.route('/', methods=['POST'])　#チャンネル追加
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

@app.route('/update_channel', methods=['POST'])　#チャンネル編集
def update_channel():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')

    cid = request.form.get('cid')
    channel_name = request.form.get('channel-title')
    channel_description = request.form.get('channel-description')

    dbConnect.updateChannel(uid, channel_name, channel_description, cid)
    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)
    return render_template('detail.html', messages=messages, channel=channel, uid=uid)


@app.route('/delete/<cid>')　#チャンネル削除
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


# uidもmessageと一緒に返す
@app.route('/detail/<cid>')　#チャットの中身
def detail(cid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    cid = cid
    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)

    return render_template('detail.html', messages=messages, channel=channel, uid=uid)


@app.route('/message', methods=['POST'])　#メッセージ投稿
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


@app.route('/delete_message', methods=['POST'])　#メッセージ削除
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

@app.route('/')　#TO DO LIST
def todolist():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    else:
        todolist = get_todolist(uid)
        return render_template('todolist.html', todolist=todolist, uid=uid)

@app.route('/add_task', methods=['POST']) #taskを作成
def add_task():
    uid = session.get('uid')
    if uid is None:
        return redirect('/login')
    title = request.form.get('title')
    if title:
        add_task_list(uid, title)
    return redirect('/')

@app.route('/delete_task', methods=['POST'])　#taskを削除
def delete_task():
    uid = session.get('uid')
    if uid is None:
        return redirect('/login')
    tid = request.form.get('tid')
    if tid:
        delete_task_list(uid, tid)
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



