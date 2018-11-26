from flask import render_template, url_for, redirect, flash, request
from flaskblog import app,db,bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UserSearchForm, Results
from flaskblog.models import User
from flask_login import login_user, current_user, logout_user

@app.route("/",methods = ['GET','POST'])
@app.route("/home",methods = ['GET','POST'])
def home():
    form = UserSearchForm()
    if current_user.is_authenticated:
        if current_user.username == 'doctor_user':
            search = UserSearchForm(request.form)
            if request.method == 'POST':
                return search_results(search)
            
            return render_template('index.html', form = search)
        else:
            return render_template('user.html')
    else:
        return render_template('home.html')


@app.route('/results')
def search_results(search):
    '''
    form = UserSearchForm()
    results =[]
    results = User.query.filter_by(username = form.username.data).first()
    if not results:
        flash('No results found!')
        return redirect(url_for('home'))
    else:
        return render_template('DocPage.html',results = results)
    return render_template('index.html')
'''
    results=[]
    search_string = search.data['search']

    if search.data['search'] == '':
        user = User.query.all()
        results = user

    #else:
    #    user1 = User.query.filter_by(username = form.username.data)
    #    for i in user1:
    #        result.append(i)
    #    results = User.query.filter_by('select')

    

    if not results:
        flash('No results found!')
        return redirect('/home')

    else:
        return render_template('DocPage.html',results = results)



@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register",methods = ['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))        #So, if a user has been authenticated, then they won't need to visit the login or register page and will be redirected to the home page.
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email = form.email.data, password = hash_password, age = form.age.data, gender = form.gender.data, phone = form.phone.data, address = form.address.data, height = form.height.data, weight = form.weight.data, bloodgroup = form.bloodgroup.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title= 'Register' , form = form)

@app.route("/login", methods = ['GET' , 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        #if form.username.data == 'doctor_user' and form.password.data == 'superpassword':#bcrypt.check_password_hash(user.password, superpassword):
        #    return redirect(url_for('home'))
        #else:
        user = User.query.filter_by(username = form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Unsuccessful login. Check your username and password')
    return render_template('login.html', title= 'Login' , form = form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

