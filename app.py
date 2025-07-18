from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'harshithbhaskar'

# Configure MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:sudheer%40123@localhost/farmers'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ------------------- MODELS -------------------

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class Farming(db.Model):
    fid = db.Column(db.Integer, primary_key=True)
    farmingtype = db.Column(db.String(100))

class Addagroproducts(db.Model):
    pid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))
    productname = db.Column(db.String(100))
    productdesc = db.Column(db.String(300))
    price = db.Column(db.Integer)

class Trig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fid = db.Column(db.String(100))
    action = db.Column(db.String(100))
    timestamp = db.Column(db.String(100))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(1000))

class Register(db.Model):
    rid = db.Column(db.Integer, primary_key=True)
    farmername = db.Column(db.String(50))
    adharnumber = db.Column(db.String(50))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(50))
    phonenumber = db.Column(db.String(50))
    address = db.Column(db.String(50))
    farming = db.Column(db.String(50))

# ------------------- ROUTES -------------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email Already Exists", "warning")
            return render_template('signup.html')

        encpassword = generate_password_hash(password)
        new_user = User(username=username, email=email, password=encpassword)
        db.session.add(new_user)
        db.session.commit()
        flash("Signup Successful! Please Login", "success")
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Login Successful", "primary")
            return redirect(url_for('index'))
        else:
            flash("Invalid credentials", "danger")
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout Successful", "warning")
    return redirect(url_for('login'))

@app.route('/register', methods=['POST', 'GET'])
@login_required
def register():
    farming = Farming.query.all()
    if request.method == "POST":
        farmername = request.form.get('farmername')
        adharnumber = request.form.get('adharnumber')
        age = request.form.get('age')
        gender = request.form.get('gender')
        phonenumber = request.form.get('phonenumber')
        address = request.form.get('address')
        farmingtype = request.form.get('farmingtype')

        new_record = Register(
            farmername=farmername,
            adharnumber=adharnumber,
            age=age,
            gender=gender,
            phonenumber=phonenumber,
            address=address,
            farming=farmingtype
        )
        db.session.add(new_record)
        db.session.commit()
        flash("Record Saved Successfully", "success")
        return redirect('/farmerdetails')
    return render_template('farmer.html', farming=farming)

@app.route('/farmerdetails')
@login_required
def farmerdetails():
    query = Register.query.all()
    return render_template('farmerdetails.html', query=query)

@app.route('/edit/<string:rid>', methods=['POST', 'GET'])
@login_required
def edit(rid):
    farming = Farming.query.all()
    post = Register.query.filter_by(rid=rid).first()
    if request.method == "POST":
        post.farmername = request.form.get('farmername')
        post.adharnumber = request.form.get('adharnumber')
        post.age = request.form.get('age')
        post.gender = request.form.get('gender')
        post.phonenumber = request.form.get('phonenumber')
        post.address = request.form.get('address')
        post.farming = request.form.get('farmingtype')
        db.session.commit()
        flash("Record Updated", "success")
        return redirect('/farmerdetails')
    return render_template('edit.html', posts=post, farming=farming)

@app.route('/delete/<string:rid>', methods=['POST', 'GET'])
@login_required
def delete(rid):
    Register.query.filter_by(rid=rid).delete()
    db.session.commit()
    flash("Record Deleted", "danger")
    return redirect('/farmerdetails')

@app.route('/addfarming', methods=['POST', 'GET'])
@login_required
def addfarming():
    if request.method == "POST":
        farmingtype = request.form.get('farming')
        if Farming.query.filter_by(farmingtype=farmingtype).first():
            flash("Farming Type Already Exists", "warning")
        else:
            new_farming = Farming(farmingtype=farmingtype)
            db.session.add(new_farming)
            db.session.commit()
            flash("Farming Type Added", "success")
    return render_template('farming.html')

@app.route('/addagroproduct', methods=['POST', 'GET'])
@login_required
def addagroproduct():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        productname = request.form.get('productname')
        productdesc = request.form.get('productdesc')
        price = request.form.get('price')
        print("DEBUG:", username, email, productname, productdesc, price) 

        new_product = Addagroproducts(
            username=username,
            email=email,
            productname=productname,
            productdesc=productdesc,
            price=price
        )
        db.session.add(new_product)
        db.session.commit()
        flash("Product Added", "info")
        return redirect('/agroproducts')
    return render_template('addagroproducts.html')

@app.route('/agroproducts')
def agroproducts():
    query = Addagroproducts.query.all()
    return render_template('agroproducts.html', query=query)

@app.route('/triggers')
@login_required
def triggers():
    query = Trig.query.all()
    return render_template('triggers.html', query=query)

@app.route('/test')
def test():
    try:
        Test.query.all()
        return 'Database Connected'
    except:
        return 'Database Not Connected'

# ------------------- RUN APP -------------------

if __name__ == '__main__':
    app.run(debug=True)
