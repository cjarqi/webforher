# app/routes.py

from flask import Blueprint, render_template, request, redirect, url_for
from app import db  # Import the db object
from sqlalchemy import text # To execute raw SQL safely

bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        author = request.form['author']
        message = request.form['message']
        
        # SQLAlchemy handles the connection for us
        sql = text("INSERT INTO notes (author, message) VALUES (:author, :message)")
        db.session.execute(sql, {"author": author, "message": message})
        db.session.commit()
        
        return redirect(url_for('main.index'))

    # Execute a query to get your notes
    sql_my_notes = text("SELECT * FROM notes WHERE author = :author ORDER BY created_at DESC LIMIT 4")
    my_notes_result = db.session.execute(sql_my_notes, {"author": "Cj"}).mappings().all()

    # Execute a query to get the total count
    sql_count = text("SELECT COUNT(id) AS note_count FROM notes WHERE author = :author")
    note_count = db.session.execute(sql_count, {"author": "Cj"}).scalar_one()

    return render_template('index.html', my_notes=my_notes_result, note_count=note_count)


@bp.route('/secret-notes', methods=['GET', 'POST'])
def view_her_notes():
    if request.method == 'POST':
        author = request.form['author']
        message = request.form['message']
        
        sql = text("INSERT INTO notes (author, message) VALUES (:author, :message)")
        db.session.execute(sql, {"author": author, "message": message})
        db.session.commit()
        
        return redirect(url_for('main.view_her_notes'))

    # Fetch her notes
    sql_her_notes = text("SELECT * FROM notes WHERE author = :author ORDER BY created_at DESC")
    her_notes = db.session.execute(sql_her_notes, {"author": "Angel"}).mappings().all()
    
    # Fetch your notes
    sql_my_notes = text("SELECT * FROM notes WHERE author = :author ORDER BY created_at DESC")
    my_notes = db.session.execute(sql_my_notes, {"author": "Cj"}).mappings().all()

    return render_template('her_notes.html', her_notes=her_notes, my_notes=my_notes)


@bp.route('/my-notes')
def all_notes_for_her():
    sql_my_notes = text("SELECT * FROM notes WHERE author = :author ORDER BY created_at DESC")
    my_notes = db.session.execute(sql_my_notes, {"author": "Cj"}).mappings().all()
    
    return render_template('all_my_notes.html', my_notes=my_notes)