from flask import Flask, render_template, redirect, request, session, flash
from werkzeug.security import check_password_hash, generate_password_hash
from models import dbConnect, User
import uuid

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # セッションで使用する秘密鍵を設定します

@app.route('/')
def index():
    if 'user_id' not in session:  # ユーザーが認証されていない場合はログインページにリダイレクトします
        return redirect('/login')
    user_id = session['user_id']
    user = dbConnect.get_user(user_id)  # ログイン中のユーザーを取得します
    return render_template('index.html', user=user)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if not (name and email and password and confirm_password):
            flash('入力フォームが未入力です')
        elif password != confirm_password:
            flash('パスワードが一致しません')
        elif dbConnect.get_user_by_email(email):
            flash('既に登録されているメールアドレスです')
        else:
            user_id = uuid.uuid4().hex
            hashed_password = generate_password_hash(password)
            user = User(user_id, name, email, hashed_password)
            dbConnect.create_user(user)
            session['user_id'] = user_id
            return redirect('/')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = dbConnect.get_user_by_email(email)
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.uid
            return redirect('/')
        else:
            flash('メールアドレスまたはパスワードが違います')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)  # セッションからユーザーIDを削除します
    return redirect('/login')




