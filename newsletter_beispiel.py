from flask import Flask, render_template, request

from verwaltung import (
    add_person,
    delete_person,
    get_person_for_id,
    get_persons,

)

app = Flask(__name__)


# Startseite
@app.route('/')
def index():
    return render_template('index.html')

# Anmeldeformular verarbeiten
@app.route('/anmelden', methods=['GET', 'POST'])
def anmeldung():
    if request.method == "POST":
        try:
            email = request.form.get('email')
            vorname = request.form.get('vorname')
            nachname = request.form.get('nachname')
            id = add_person(email, vorname, nachname)
        except ValueError or '@' not in email:
            return "Eingabefehler", 400
        
        #Ergebnisseite anzeigen
        return render_template("anmeldung.html", email=email, vorname=vorname, nachname=nachname)
    return render_template("index.html")

@app.route("/delete/<id>")
def delete(id):
    # notwendig, um Information zur gelöschten Person ausgeben zu können.
    person = get_person_for_id(id)
    delete_person(id)
    return render_template("delete.html", name=person.name, id=person.id)

# Adminseite, zeigt alle Abonnenten an
@app.route('/admin')
def anzeigen():
    anmeldungen= get_persons()
    return render_template('admin.html', anmeldung=anmeldung)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
