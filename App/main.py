from flask import Flask, render_template, request, session, make_response, escape
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash 
from flask import session
#Presentado Por:
#Natalia Hernandez
#Leidy Quintero
#Maurico Lopez
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.secret_key = '123456'

class Usuarios(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(50),nullable=True)
	apellido = db.Column(db.String(50),nullable=True)
	email = db.Column(db.String(50), unique=True, nullable=True)
	contrasena = db.Column(db.String(80), nullable=True)

class contacto(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(50),nullable=True)
	apellido = db.Column(db.String(50),nullable=True)
	email = db.Column(db.String(50), nullable=True)
	descripcion = db.Column(db.String(250), nullable=True)
		
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/service')
def service():
	return render_template('service.html')


def validar_datos(usuario):
	if len(usuario) <= 5:
		return "Usuario No Válido"

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		nombre = request.form['nombre']
		apellido = request.form['apellido']
		email = request.form['email']
		contrasena = request.form['contrasena']

		contrasena_encriptada = generate_password_hash(contrasena,method='sha256')
		nuevo_usuario = Usuarios(nombre=nombre,apellido=apellido,email=email,contrasena=contrasena_encriptada)
		db.session.add(nuevo_usuario)
		db.session.commit()
		return render_template('home.html')
	return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form['email']
		contrasena = request.form['contrasena']
		email = Usuarios.query.filter_by(email=email).first()

		if email and check_password_hash(email.contrasena,contrasena):
			session['email'] = email.email
			return render_template('home.html')
		return render_template('login.html')
	return render_template('login.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	if request.method == 'POST':
		nombre = request.form['nombre']
		apellido = request.form['apellido']
		email = request.form['email']
		descripcion = request.form['descripcion']

		nuevo_contacto = contacto(nombre=nombre,apellido=apellido,email=email,descripcion=descripcion)
		db.session.add(nuevo_contacto)
		db.session.commit()
		return render_template('index.html')
	return render_template('contact.html')

@app.route('/home')
def home():
	if "email" in session:
		return render_template('home.html')
	return render_template('login.html')
def cerrar():
	#session.pop('email',None)
	#session.pop('contrasena',None)
	#logout_user()
	#return request.session.delete()
	session.clear()
	return render_template('index.html')

if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)