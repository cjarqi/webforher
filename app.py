# app.py

from flask import Flask, render_template, request, redirect, url_for
import flask_mysql_connector

app = Flask(__name__)

# --- IMPORTANT: DATABASE CONFIGURATION ---
# Replace the placeholder values with your actual MySQL credentials.
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'cjarqi'
app.config['MYSQL_DATABASE'] = 'gift_website'

mysql = flask_mysql_connector.MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        author = request.form['author']
        message = request.form['message']
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notes (author, message) VALUES (%s, %s)", (author, message))
        conn.commit()
        cursor.close()
        return redirect(url_for('index'))

    conn = mysql.connection
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM notes WHERE author = %s ORDER BY created_at DESC LIMIT 4", ('Cj',))
    my_notes = cursor.fetchall()
    
    cursor.execute("SELECT COUNT(id) AS note_count FROM notes WHERE author = %s", ('Cj',))
    note_count = cursor.fetchone()['note_count']

    cursor.close()

    return render_template('index.html', my_notes=my_notes, note_count=note_count)


@app.route('/secret-notes', methods=['GET', 'POST'])
def view_her_notes():
    if request.method == 'POST':
        author = request.form['author']
        message = request.form['message']
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notes (author, message) VALUES (%s, %s)", (author, message))
        conn.commit()
        cursor.close()
        return redirect(url_for('view_her_notes'))

    conn = mysql.connection
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM notes WHERE author = %s ORDER BY created_at DESC", ('Angel',))
    her_notes = cursor.fetchall()
    cursor.execute("SELECT * FROM notes WHERE author = %s ORDER BY created_at DESC", ('Cj',))
    my_notes = cursor.fetchall()
    cursor.close()
    return render_template('her_notes.html', her_notes=her_notes, my_notes=my_notes)


@app.route('/my-notes')
def all_notes_for_her():
    conn = mysql.connection
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM notes WHERE author = %s ORDER BY created_at DESC", ('Cj',))
    my_notes = cursor.fetchall()
    cursor.close()
    return render_template('all_my_notes.html', my_notes=my_notes)


if __name__ == '__main__':
    app.run(debug=True)