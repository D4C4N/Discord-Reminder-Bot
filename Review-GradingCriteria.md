#  Review: ToDoListPythonProject
[ToDoListPythonProject](https://github.com/Tim10022023/ToDoListPythonProject)
This project was made by [Wildeswiesel](https://github.com/Wildeswiesel), [Tim10022023](https://github.com/Tim10022023) and [nklshpf](https://github.com/nklshpf).

It is about a To-Do List made through a website.

Review made by [Daniel](https://github.com/D4C4N) and [Sven](https://github.com/SvenSrc)

# Grading Criteria Programmieren T3INF1004
In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.
Alle Kriterien betreffen nur die Projektarbeit. Beweismaterial kommt aus dem Gruppenprojekt.

## FACHKOMPETENZ (40 Punkte)

# Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)
<!-- Siehe Kenntnisse in prozeduraler Programmierung: zutreffendes wählen und beweisen-->

## Variablen Deklaration
Im Projekt werden Variablen deklariert mit sinnvollen Namen.
Anbei einige Beispiele:

```Python
    username = request.form.get('username')
    password = request.form.get('password')
```

## Einsatz von Bibliotheken
Es werden Bibliotheken miteingebunden

```Python
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_wtf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Task, User, UserMixin
from datetime import datetime, timedelta
```

# Sie können die Syntax und Semantik von Python (10)
<!-- Eine Stelle aus ihrem Programmieren wählen auf die sie besonders stolz sind und begründen -->

## Einsatz von for-Schleifen
Der unten stehende Code prüft welche Tasks frühzeitig gemacht werden soll.

```Python
tasks = Task.query.all()
for task in tasks:
    task.due_soon = check_due_date(task.date)
```

## Einsatz von If und else
Dieser Abteil ist für den Login zuständig. Es schaut nach ob 'user' und 'password' gleich sind. Wenn sie gleich sind, wird man zur homepage gebracht.
Sonst bekommt man die Nachricht, dass es etwas falsch ist.

```Python
if user and check_password_hash(user.password_hash, password):
    login_user(user)
    return redirect(url_for('homepage'))
else:
    flash('Ungültiger Benutzername oder Passwort.')
```

# Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)
<!-- Anhand von commits zeigen, wie jeder im Projekt einen Beitrag geleistet hat -->

![Screenshot 2024-02-26 145334](https://github.com/D4C4N/Discord-Reminder-Bot/assets/69164233/f5b1abe0-eccf-4f75-94f9-501cc9167c72)



# Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)
<!-- Eine Stelle aus dem Projekt wählen auf die sie besonders stolz sind und begründen -->
Sie können einmal mit eienr Datenbank kommunizieren sowie auch mit den Daten von einer Datenbank umgehen. Einiger werden beispielsweise in einem Array gespeichert.

```Python
    users = User.query.all()
    task_content=[]
    task_date=[]
    task_done=False
    if request.method == 'POST' and current_user.is_authenticated:
        task_content = request.form["content"]
        task_date = request.form["date"]
        assigned_to = request.form.get('assigned_to')
        task_done = 'done' in request.form
       
        new_task = Task(content=task_content, date=task_date, user_id=assigned_to,  assigned_by_id=current_user.id, done=task_done)
        db.session.add(new_task)
        db.session.commit()
```

## METHODENKOMPETENZ (10 Punkte)

# Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)
<!-- Beweise anbringen für Nutzen folgender Tools (können links, screenshots und screnncasts sein) -->

<!-- zB -->
<!-- GIT -->
<!-- VSC -->
<!-- Copilot -->
<!-- other -->
Die Gruppe kann mit den folgenden Tools umgehen:

* GIT
* VSC
* DB-Browser für SQLite

GIT wird nachgewiesen durch die Verwendung von Github.
Falls sie was anderes außer VS-Code verwendet haben, ist es sogar umso besser.
SQLite wird nachgewiesen, durch ihr Projekt.

## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

# Die Studierenden können ihre Software erläutern und begründen. (5)
<!-- Jeder in der Gruppe: You have helped someone else and taught something to a fellow student (get a support message from one person) -->

Dieser Punkt ist schwer nachzuweisen, da wir keinen Einblick haben von dieser Gruppe über jedes Problem.

Allerdings steht auf der dazugehörigen Gruppe in der Grading Criteria folgender Text:

Noah: Probleme mit Github -> Branch konnte nicht gemerget werden (erklärt online mit Bildschirm) Tim: Datenbank konnte nicht geleseen werden -> hat db.session.commit() gefehlt, Namensgebung in der DB angepasst Niklas: Im HTML Problem dass die Popup-Seite nicht geschlossen wird wenn auf Save geklickt wird, wurde gelöst durch return "<script>window.opener.location.reload(); window.close();</script>" in der app.py datei

# Sie können existierenden Code analysieren und beurteilen. (5)
<!-- Pro Gruppe:You have critiqued another group project. Link to your critique here (another wiki page on your git) and link the project in the critique, use these evaluation criteria to critique the other project. Make sure they get a top grade after making the suggested changes -->

[ToDoListPythonProject](https://github.com/Tim10022023/ToDoListPythonProject)

# Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)
<!-- Which technology did you learn outside of the teacher given input -->
<!-- Did you or your group get help from someone in the classroom (get a support message here from the person who helped you) -->

* Flask (flask, flask_login)
* DB (flask_sqlalchemy)
* CSRFProtection (flask_wtf)
* Password-Hash (werkzeug.security)

Flask kann nachgewiesen werden, durch die Einbindung von Python Code auf einer Website.
DB kann nachgewiesen werden, durch ihr Projekt.
CSFRProtection und Password-Hash kann auch nachgewiesen werden durch ihr Projekt und der funktionierenden Login Seite.

## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

# Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)
<!-- Which parts of your project are you proud of and why (describe, analyse, link) -->
<!-- Where were the problems with your implementation, timeline, functionality, team management (describe, analyse, reflect from past to future, link if relevant) -->

Der folgende Code gefällt uns persönlich aus dem Grund, weil es mehrere fundamentale Grundkenntnisse des Programmierens mit einbindet.


```Python
def delete_user():
    user_ids = request.form.getlist('user_ids')
    for user_id in user_ids:
        user = User.query.get_or_404(user_id)
        if user == current_user:
            flash('Sie können sich nicht selbst löschen.')
        else:
            # Löschen aller Aufgaben, die dem Benutzer zugeordnet sind
            Task.query.filter((Task.user_id == user_id) | (Task.assigned_by_id == user_id)).delete()
            
            # Jetzt den Benutzer löschen
            db.session.delete(user)
    db.session.commit()
    return redirect(url_for('homepage'))
```

Erstens haben wir eine Function, dass daraufhin zu einer Variablen Deklaration führt.
Weiterhin wird mit einem For-Loop die Benutzer entnommen.
Es wird dann geprüft ob man dieser Benutzer ist, oder nicht. Falls Ja, kommt die Nachricht, dass man sich nicht selbst löschen kann, sonst kann man es löschen und alle dazugehörigen Aufgaben.

## Kenntnisse in prozeduraler Programmierung:

# Algorithmenbeschreibung
```Python
def check_due_date(task_date_string):
    if not task_date_string:  # Überprüft, ob der String leer ist
        return False  # oder eine andere geeignete Antwort
    task_date = datetime.strptime(task_date_string, "%Y-%m-%d").date()
    due_date = datetime.now().date() + timedelta(days=1)
    return task_date <= due_date
```
# Datentypen

```Python
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(255), nullable=False)
    done = db.Column(db.Boolean, default=False)
```

# - E/A-Operationen und Dateiverarbeitung

```Python
from models import db, Task, User, UserMixin

task_content = request.form ["Inhalt"]
```

## Input
```Python
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
```
Input waren der 'username' und 'password'

## Output
```Python
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('homepage'))
        else:
            flash('Ungültiger Benutzername oder Passwort.')
    return render_template('login.html') 
```
Output ist abhängig, ob der obige Input übereinstimmt.
Falls der übereinstimmt, kommt man zur Homepage, sonst bekommt man eine Nachricht, dass etwas falsch ist.

# Operatoren

```Python
 if request.method == 'POST' and current_user.is_authenticated:
```
```Python
 if Benutzer and check_password_hash (user.password_hash, Passwort):
```
```Python
 Task.query.filter((Task.user_id == user_id) | (Task.assigned_by_id == user_id)).delete()
```

# Kontrollstrukturen
```Python
if user == current_user:
    flash('Sie können sich nicht selbst löschen.')
```
# Funktionen

```Python
@app.route('/delete_task', methods=['POST'])
def delete_task():
    task_ids = request.form.getlist('task_ids')
    for task_id in task_ids:
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
    db.session.commit()
    return redirect(url_for('homepage'))
```

# Stringverarbeitung
```Python
    username = request.form.get('username')
    password = request.form.get('password')
    ...
    new_user = User(username=username, password_hash=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
```
# Strukturierte Datentypen

```Python
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(255), nullable=False)
    done = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 
    assigned_by_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  

    user = db.relationship('User', foreign_keys=[user_id], backref=db.backref('tasks', lazy=True))
    assigned_by = db.relationship('User', foreign_keys=[assigned_by_id], backref=db.backref('assigned_tasks', lazy=True))
```
