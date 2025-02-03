from flask import Flask, render_template, redirect, request, make_response
import json

# App-Objekt erstellen
app = Flask('NewsletterApp')

# Hilfsfunktionen zum Laden und Speichern der Daten
def laden():
    f = open('newsletter.json', 'r')
    return json.load(f)

def speichern(data):
    f = open('newsletter.json', 'w')
    json.dump(data, f, indent=2)
    f.close()

# Startseite
@app.route('/')
def index():
    return render_template('index.html')

# Anmeldeformular verarbeiten
@app.route('/anmelden', methods=['POST'])
def anmeldung():
    # Daten aus dem Formular holen
    email = request.form['email']
    vorname = request.form['vorname']
    nachname = request.form['nachname']

    # ein möglicher, aber noch nicht ausreichender Test auf eine gültige E-Mail-Adresse
    if '@' not in email:
        # im Fehlerfall wird ein HTTP-Statuscode 400 zurückgegeben
        return "Keine gültige E-Mail", 400

    # bisherige Daten aus der Datei laden
    daten = laden()

    # neues Dictionary mit den Daten des neuen Abonnenten
    daten.append({
        "email": email,
        "vorname": vorname,
        "nachname": nachname
    })

    # speichern der Daten in der Datei
    speichern(daten)

    # Ergebnisseite anzeigen
    return render_template('anmeldung.html', email=email, vorname=vorname, nachname=nachname)

# Adminseite, zeigt alle Abonnenten an
@app.route('/admin')
def admin():
    daten = laden()
    return render_template('admin.html', daten=daten)

# Starten der Anwendung
app.run(debug=True)
