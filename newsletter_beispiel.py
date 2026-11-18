from flask import Flask, render_template, request

from verwaltung import (
    add_person,
    delete_person,
    get_person_for_id,
    get_persons,
    update_person,

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
    anmeldung = get_persons()
    return render_template("admin.html", anmeldung=anmeldung)

@app.route("/update", methods=["POST"])
def update():
    id = request.form.get("id")
    name = request.form.get("name")
    weight = request.form.get("weight")
    height = request.form.get("height")
    update_person(id, name, weight, height)
    return render_template("anmeldung.html", name=name, id=id)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
