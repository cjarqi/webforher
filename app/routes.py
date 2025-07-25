# app/routes.py

from flask import Blueprint, render_template, request, redirect, url_for
from app import mysql  # Import the mysql object from the __init__.py

# Create a Blueprint, which is a way to organize a group of related views
bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        author = request.form['author']
        message = request.form['message']
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notes (author, message) VALUES (%s, %s)", (author, message))
        conn.commit()
        cursor.close()
        return redirect(url_for('main.index'))

    conn = mysql.connection
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM notes WHERE author = %s ORDER BY created_at DESC LIMIT 4", ('Cj',))
    my_notes = cursor.fetchall()
    
    cursor.execute("SELECT COUNT(id) AS note_count FROM notes WHERE author = %s", ('Cj',))
    note_count = cursor.fetchone()['note_count']

    cursor.close()

    return render_template('index.html', my_notes=my_notes, note_count=note_count)


@bp.route('/secret-notes', methods=['GET', 'POST'])
def view_her_notes():
    if request.method == 'POST':
        author = request.form['author']
        message = request.form['message']
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notes (author, message) VALUES (%s, %s)", (author, message))
        conn.commit()
        cursor.close()
        return redirect(url_for('main.view_her_notes'))

    conn = mysql.connection
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM notes WHERE author = %s ORDER BY created_at DESC", ('Angel',))
    her_notes = cursor.fetchall()
    cursor.execute("SELECT * FROM notes WHERE author = %s ORDER BY created_at DESC", ('Cj',))
    my_notes = cursor.fetchall()
    cursor.close()
    return render_template('her_notes.html', her_notes=her_notes, my_notes=my_notes)


@bp.route('/my-notes')
def all_notes_for_her():
    conn = mysql.connection
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM notes WHERE author = %s ORDER BY created_at DESC", ('Cj',))
    my_notes = cursor.fetchall()
    cursor.close()
    return render_template('all_my_notes.html', my_notes=my_notes)