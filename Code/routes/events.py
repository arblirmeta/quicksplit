# Events für unser QuickSplit Projekt

from flask import Blueprint, render_template, request, redirect, url_for, flash
import sqlite3

# Blueprint - haben wir von Stackoverflow kopiert
events_bp = Blueprint('events', __name__)

@events_bp.route('/events')
def list_events():
    """Zeigt alle Events"""
    # Datenbank öffnen
    conn = sqlite3.connect('quicksplit.db')
    conn.row_factory = sqlite3.Row
    
    # SQL Query - haben wir aus dem Internet
    events = conn.execute('SELECT * FROM events').fetchall()
    
    conn.close()
    
    return render_template('events/list.html', events=events)

@events_bp.route('/events/new', methods=['GET', 'POST'])
def create_event():
    """Event erstellen"""
    if request.method == 'POST':
        name = request.form['name']
        
        # Prüfen ob Name da ist
        if name == '':
            flash('Bitte gib einen Namen ein!')
            return render_template('events/create.html')
        
        # In Datenbank speichern
        conn = sqlite3.connect('quicksplit.db')
        conn.execute('INSERT INTO events (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()
        
        flash('Event erstellt!')
        return redirect('/events')
    
    return render_template('events/create.html')

@events_bp.route('/events/<int:event_id>')
def show_event(event_id):
    """Ein Event anzeigen"""
    conn = sqlite3.connect('quicksplit.db')
    conn.row_factory = sqlite3.Row
    
    # Event holen
    event = conn.execute('SELECT * FROM events WHERE id = ?', (event_id,)).fetchone()
    
    # Teilnehmer holen
    users = conn.execute('SELECT * FROM users WHERE event_id = ?', (event_id,)).fetchall()
    
    conn.close()
    
    if event is None:
        return "Event nicht gefunden", 404
    
    return render_template('events/show.html', event=event, users=users)


