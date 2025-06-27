# QuickSplit - Code

## Commit 2: Datenbankstruktur erstellt

Wir haben die SQLite-Datenbank für QuickSplit aufgesetzt.

### Was funktioniert:

- SQLite Datenbank wird automatisch erstellt ✅
- Tabellen: events, users, expenses, expense_participants ✅
- Foreign Keys zwischen den Tabellen ✅

### Wie testen:

1. `python app.py` starten
2. Browser zu `http://localhost:5000` 
3. Prüfen ob `quicksplit.db` Datei erstellt wurde

### Datenbankstruktur:

**events** - Speichert die Events (Urlaub, Party, etc.)
- id, name, created_at

**users** - Teilnehmer in Events  
- id, name, event_id

**expenses** - Ausgaben innerhalb von Events
- id, title, amount, date, payer_id, event_id

**expense_participants** - Wer war bei welcher Ausgabe dabei
- expense_id, user_id

### Probleme die wir hatten:

- SQLite Foreign Key Syntax war neu für uns
- Mussten nachschauen wie `IF NOT EXISTS` funktioniert
- `row_factory` haben wir aus einem Tutorial

### Nächste Schritte:

- Templates mit Bootstrap erstellen
- Formulare für Events/Users/Expenses
- Routes implementieren

---
*Arblir & Mohamed* 