from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from werkzeug.security import check_password_hash, generate_password_hash
from db_connection import create_connection

app = Flask(__name__)
app.secret_key = 'root'

# Inicializa la conexión a la base de datos
connection = create_connection()

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/inicio')
def inicio():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # Información del usuario
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT nombre FROM usuarios WHERE id = %s", (session.get('user_id'),))
    user = cursor.fetchone()

    if not user:
        return redirect(url_for('login'))

    # Tareas del usuario, ordenadas por hora
    cursor.execute("SELECT * FROM tareas WHERE user_id = %s ORDER BY hour", (session.get('user_id'),))
    tasks = cursor.fetchall()

    total_tasks = len(tasks)
    completed_tasks = len([task for task in tasks if task['completed']])
    productivity_percentage = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0

    return render_template('inicio.html', tasks=tasks, productivity_percentage=productivity_percentage, user_name=user['nombre'])

@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tareas (name, hour, user_id) VALUES (%s, %s, %s)", 
                   (data['name'], data.get('hour'), session['user_id']))
    connection.commit()
    return jsonify(success=True)

@app.route('/edit_task/<int:id>', methods=['POST'])
def edit_task(id):
    data = request.get_json()
    cursor = connection.cursor()
    cursor.execute("UPDATE tareas SET name = %s, hour = %s WHERE id = %s", 
                   (data['name'], data.get('hour'), id))
    connection.commit()
    return jsonify(success=True)

@app.route('/complete_task/<int:id>', methods=['POST'])
def complete_task(id):
    cursor = connection.cursor()
    cursor.execute("UPDATE tareas SET completed = NOT completed WHERE id = %s", (id,))
    connection.commit()
    return jsonify(success=True)

@app.route('/delete_task/<int:id>', methods=['POST'])
def delete_task(id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tareas WHERE id = %s", (id,))
    connection.commit()
    return jsonify(success=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        email = data['email']
        password = data['password']

        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            return jsonify({'status': 'success', 'message': 'Inicio de sesión exitoso'})
        else:
            return jsonify({'status': 'error', 'message': 'Correo o contraseña incorrectos'})

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        nombre = request.form.get('nombre', '').strip()
        apellido = request.form.get('apellido', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        confirm_password = request.form.get('confirmPassword', '').strip()

        if not all([username, nombre, apellido, email, password, confirm_password]):
            return jsonify({'status': 'error', 'message': 'Por favor, completa todos los campos'})

        if password != confirm_password:
            return jsonify({'status': 'error', 'message': 'Las contraseñas no coinciden'})

        try:
        
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
            existing_user = cursor.fetchone()

            if existing_user:
                return jsonify({'status': 'error', 'message': 'El correo ya está registrado'})

            hashed_password = generate_password_hash(password)

            cursor.execute(
                "INSERT INTO usuarios (username, nombre, apellido, email, password) VALUES (%s, %s, %s, %s, %s)",
                (username, nombre, apellido, email, hashed_password)
            )
            connection.commit()

            return jsonify({'status': 'success', 'message': 'Registro exitoso'})

        except Exception as e:
            return jsonify({'status': 'error', 'message': f'Error en el servidor: {str(e)}'})
        finally:
            cursor.close()

    return render_template('register.html')

@app.route('/contactos')
def contactos():
    return render_template('contactos.html')

if __name__ == '__main__':
    app.run(debug=True)
