# Discord-Reminder-Bot
A discord bot that allows users to set reminders, view reminders and mark reminders as complete. The bot also uses an API to greet new members with a joke, however that functionality is currently broken and couldn't be fixed in time for the final revision of the project.

# Grading Criteria Programmieren T3INF1004
In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.
Alle Kriterien betreffen nur die Projektarbeit. Beweismaterial kommt aus dem Gruppenprojekt.

## FACHKOMPETENZ (40 Punkte)

# Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)
<!-- Siehe Kenntnisse in prozeduraler Programmierung: zutreffendes wählen und beweisen-->

## Variablen Deklaration
Im gesamten finalen Projekt werden an unterschiedlichen Stellen Variablen deklariert. Anbei einige Beispiele:

```Python
message = ctx.message.content
...
channel = client.get_channel(CHANNEL_GENERAL)
setup = json.loads(response.text)["body"][0]["setup"]
punchline = json.loads(response.text)["body"][0]["punchline"]
```

## Verwendung von Dictionaries
Die Informationen für die Datenbank sind in einem Dictionary gespeichert.

```Python
database = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "discordbot"
)
```

## Einsatz von Bibliotheken
In das finale Projekt sind divese Bibliotheken importiert worden.

```Python
import os
from dotenv import load_dotenv
import requests
import json
import mysql.connector
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
```

# Sie können die Syntax und Semantik von Python (10)
<!-- Eine Stelle aus ihrem Programmieren wählen auf die sie besonders stolz sind und begründen -->

## Einsatz von for-Schleifen
Der untenstehende Code iteriert über Zeilen, die aus einer Datenbankabfrage stammen, und extrahiert Werte aus den Spalten "todo" und "due_to" für die weitere Verwendung im Programm.

```Python
rows = cursor.fetchall()
for row in rows:
  value_todo = row["todo"]
  value_due_to = row["due_to"]
```

## Einsatz von If und else
Dieser Code prüft, ob der Wert der Variable `value_due_to` nicht leer ist. Falls nicht, sendet er eine Nachricht, die den Wert der Variable `value_todo` und den Wert der Variable `value_due_to` in einem bestimmten Format an einen Kontext `ctx` sendet. Andernfalls sendet er nur den Wert der Variable `value_todo` an denselben Kontext `ctx`.

```Python
if(value_due_to != ""):
  await ctx.send(f'* "{value_todo}" is due to "{value_due_to}"')
else:
  await ctx.send(f'* {value_todo}')
```

## Asynchrones Programmieren
Bedingt durch die Funktionsweise eines Discord-Bots finden sich im Code zahlreiche asynchrone Funktionen. Anbei ein kurzes, stellvertretendes Beispiel. Diese Funktion removeall(ctx) verwendet einen Benutzerkontext ctx, um die ID des Autors zu erhalten. Anschließend wird ein SQL-Befehl ausgeführt, um alle Einträge in der Datenbanktabelle "todolist" zu löschen, die mit der Benutzer-ID des Autors übereinstimmen. Danach wird eine Bestätigungsnachricht an den Kontext ctx gesendet, um den Benutzer darüber zu informieren, dass alle ihre ToDos aus der Liste entfernt wurden.

```Python
async def removeall(ctx):
  author_id = ctx.user.id

  sql = "DELETE FROM todolist WHERE user_id = %s"
  value = (author_id,)
    
  cursor.execute(sql, value)

  database.commit()

  await ctx.send("All your ToDos have been removed from the list.")
```

# Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)
<!-- Anhand von commits zeigen, wie jeder im Projekt einen Beitrag geleistet hat -->
Die Nutzung von Git kann dem untenstehenden Screenshot für das Repository entnommen werden. Selbstverständlich kann das Repository auch selbstständig auf Commits untersucht werden.

![Commits](https://i.imgur.com/YmBaGBa.png)


# Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)
<!-- Eine Stelle aus dem Projekt wählen auf die sie besonders stolz sind und begründen -->
In der Implementierung der Slash-Befehle für die Verwaltung der ToDo-Liste in unserem Discord-Bot sind wir besonders stolz. Diese Funktionen ermöglichen es den Benutzern, ihre Aufgaben einfach über die Discord-Oberfläche zu verwalten, indem sie Befehle wie "/todo" zum Hinzufügen neuer Aufgaben, "/list" zum Anzeigen aller Aufgaben und "/remove" zum Entfernen spezifischer Aufgaben verwenden. Die Verwendung von Slash-Befehlen bietet eine benutzerfreundliche und intuitive Benutzererfahrung und demonstriert unsere effektive Anwendung von Nextcord-Bibliotheksfunktionen für die Interaktion mit Benutzern in Discord.

```Python
@client.slash_command(guild_ids=[SERVER_ID], description="Our bot will greet you because he's nice :)")
async def hello(interaction: Interaction):
  member = interaction.user.mention
  await interaction.response.send_message(f"Hello, {member}! I am a bot.")
```

## Verarbeitung von Strings
```Python
# Due to
@client.command()
async def due(ctx):
  author_id = ctx.author.id

  message = ctx.message.content
  taskSplit = ' '.join(message.split()[1:-1])
  dueToSplit = ' '.join(message.split()[-1:])
```
In diesem Teil vom Code wird die Nachricht, die der Discord Bot erhält, aufgeteilt. Das heißt, wenn der Discord Bot das folgende bekommt `.due Finish Coding Project Monday`, dann sieht es so aus:
```Python
taskSplit = Finish Coding Project
dueToSplit = Monday
```
Das `.due` wird abgeschnitten vom ganzen String, weil wir das nicht brauchen in der Datenbank.
Folglich wird die Zeile in der gewünschten Tabelle geupdated mit dem Datum.

## METHODENKOMPETENZ (10 Punkte)

# Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)
<!-- Beweise anbringen für Nutzen folgender Tools (können links, screenshots und screnncasts sein) -->

<!-- zB -->
<!-- GIT -->
<!-- VSC -->
<!-- Copilot -->
<!-- other -->
Es wurden diverse Tools verwendet, unter anderem Git (offensichtlich, wir befinden uns in dem Repo.). Anbei noch Screenshots, die die Verwendung von Visual Studio Code sowie Tools, wie ChatGPT nachweisen.

**Visual Studio Code:**
![VSC](https://i.imgur.com/4iZMXy6.png)

**ChatGPT**
![ChatGPT](https://i.imgur.com/jQy0atk.png)


## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

# Die Studierenden können ihre Software erläutern und begründen. (5)
<!-- Jeder in der Gruppe: You have helped someone else and taught something to a fellow student (get a support message from one person) -->
Dieser Abschnitt ist schwer nachzuweisen. Als Gruppenmitglieder haben wir uns gegenseitig bei der Verständnisvertiefung geholfen. Themen, zu denen wir uns insbesondere ausgetauscht haben und uns gegenseitig erklärt haben waren:
- Die Verwendung von APIs 
- Die Einbindung von Datenbanken

Ansonsten wurde dieses Ziel während den wöchentlichen Coding unter unseren Blog-Einträgen vertieft. Beispielsweise möchten wir [hier](https://github.com/D4C4N/ProgrammingDaniel/discussions/10) einen Blog-Eintrag verlinken, unter welchem Verbesserungsvorschläge und Kritik zu finden sind.

# Sie können existierenden Code analysieren und beurteilen. (5)
<!-- Pro Gruppe:You have critiqued another group project. Link to your critique here (another wiki page on your git) and link the project in the critique, use these evaluation criteria to critique the other project. Make sure they get a top grade after making the suggested changes -->
**Kritik für andere Gruppen:**

Für ToDoListProject:

[Critique for the group ToDoListPythonProject](https://github.com/SvenSrc/Programming-Habit/wiki/Critique-for-the-group:-ToDoListPythonProject) 

Für Weathersite:

[Critique for the group Weathersite](https://github.com/SvenSrc/Programming-Habit/wiki/Critique-for-the-group:-Weathersite)

**Kritik zu unser Projekt von anderen:**

Von ToDoListProject:


[Critique for the group: Discord‐Reminder‐Bot](https://github.com/Tim10022023/ToDoListPythonProject/wiki/Critique-for-the-group:-Discord%E2%80%90Reminder%E2%80%90Bot)

Von Weathersite:

[Critique for group: Discord‐Reminder‐Bot](https://github.com/brudermaggi/weathersite/wiki/Critique-for-group:-Discord%E2%80%90Reminder%E2%80%90Bot)


# Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)
<!-- Which technology did you learn outside of the teacher given input -->
<!-- Did you or your group get help from someone in the classroom (get a support message here from the person who helped you) -->

* Discord-API
* Other APIs
* MySQL
* Advanced libraries, like Nextcord
* Asynchronous functions
* ... and many more

Während unser wöchentlichen Abendsitzungen haben wir uns teilweise mit anderen Gruppen über unser Projekt ausgetauscht und verbal Verbesserungsvorschläge bekommen. Wie genau wir das nachweisen sollen, das soll mir ein Rätsel bleiben.

## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

# Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)
<!-- Which parts of your project are you proud of and why (describe, analyse, link) -->
<!-- Where were the problems with your implementation, timeline, functionality, team management (describe, analyse, reflect from past to future, link if relevant) -->

Ein großes Problem war die Syntax von SQL zu verstehen. Anstatt zu erläutern wo der Fehler liegt, sagt das Programm es gab ein Fehler in der Syntax, obwohl es richtig aussah.
Ein Beispiel dazu wäre die Datenbank sicher zu machen vor SQL-Injections.
```Python
cursor.execute(f'DELETE FROM todolist WHERE todo = ("{toDeleteSplit}")')
```
Dieser Command wäre verwundbar zu SQL-Injections, weil die Variable "toDeleteSplit" nicht mit einem Platzhalter "%s" verwendet wird. Das heißt es wird eins zu eins war in dem Command steht geschickt. Was nicht gut ist.
Deshalb muss man es so umschreiben:
```Python
  sql = "DELETE FROM todolist WHERE todo = %s"
  value = (toDeleteSplit,)

  cursor.execute(sql, value)
```
Und hier kommen wir auch zu der Syntax. Es gab **immer** ein Error wenn nach dem toDeleteSplit kein Komma steht in value.
```Python
value = (toDeleteSplit)
```
Das gibt ein Syntax error
![Screenshot 2024-02-11 114852](https://github.com/D4C4N/Discord-Reminder-Bot/assets/69164233/b11c05a6-d1dd-4ab9-a898-bdd244cf3cb6)

Der Fehler wurde aber mithilfe von ChatGPT gefunden.
![Screenshot 2024-02-11 115028](https://github.com/D4C4N/Discord-Reminder-Bot/assets/69164233/e823c6a6-3ad5-41dc-8542-a508b470742f)

Weiterhin gab es ein Logik Fehler in der Datenbank. Es war am Anfang gedacht, dass wir zwei verschieden Tabellen brauchen. Eine wo nur die User-IDs stehen und bei der anderen die Todos. Die Todos werden dann mit der ersten Tabelle verknüpft. Allerdings ist uns dann später aufgefallen, dass die erste Tabelle in unserem Code nicht einmal aufgerufen wird aber trotzdem alles funktioniert. Daraufhin haben wir diese dann gelöscht.

Noch ein Problem war, dass wir die Methode send() wie ein print() Method verwendet haben. Bedeutet, wir haben der send() Method zu viele Argumente geschickt, was diese nicht kann.
![Screenshot 2024-02-09 154428](https://github.com/D4C4N/Discord-Reminder-Bot/assets/69164233/acf7f2a2-b376-4fd9-b628-2f485c249f7a)


## Kenntnisse in prozeduraler Programmierung:

# Algorithmenbeschreibung
[RSA-Algorithm](https://github.com/SvenSrc/Programming-Habit/discussions/12)

# Datentypen

## Kann String, Integer oder anderes sein
```Python
message = ctx.message.content
```

## Dictionaries
```Python
database = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "discordbot"
)
```

# - E/A-Operationen und Dateiverarbeitung
Im unten aufgeführten Beispiel wird ein User-Input verarbeitet und in einer Datenbank gespeichert.

```Python
async def todo(ctx, *, todo_item: str):
  # Extract the todo item from the commandclear
  messageSplit = todo_item

  # Check if the todo item already exists for the user
  sql_check = "SELECT todo FROM todolist WHERE user_id = %s AND todo = %s"
  value_check = (ctx.user.id, messageSplit)
  cursor.execute(sql_check, value_check)
  existing_item = cursor.fetchone()

  if existing_item:
    await ctx.send("This item is already in the list.")
  else:
    # Insert the todo item into the database
    sql_insert = "INSERT INTO todolist (todo, user_id) VALUES (%s, %s)"
    value_insert = (messageSplit, ctx.user.id)
    cursor.execute(sql_insert, value_insert)
    database.commit()

    await ctx.send(f"Added {messageSplit} to your ToDo-List!")
```

## Input
```Python
@client.command()
async def remove(ctx):
  toDelete = ctx.message.content
  toDeleteSplit = ' '.join(toDelete.split()[1:])
```
Aus `.remove This Task` im Discord Chat wird zu `This Task`


## Output
```Python
  await ctx.send(f'Removed "{toDeleteSplit}" from the list.')   
```
Vom Discord Bot kommt die Nachricht `Removed "This Task" from the list.`.

# - Operatoren

## !=
```Python
    if(value_due_to != ""):
      await ctx.send(f'* "{value_todo}" is due to "{value_due_to}"')
    else:
      await ctx.send(f'* {value_todo}')
```

# Kontrollstrukturen
```Python
    if(value_due_to != ""):
      await ctx.send(f'* "{value_todo}" is due to "{value_due_to}"')
    else:
      await ctx.send(f'* {value_todo}')
```
# Funktionen

```Python
async def removeall(ctx):
  author_id = ctx.author.id

  sql = "DELETE FROM todolist WHERE user_id = %s"
  value = (author_id,)
    
  cursor.execute(sql, value)

  database.commit()

  await ctx.send("Cleared the List.")
```

# Stringverarbeitung
```Python
  author_id = ctx.author.id

  message = ctx.message.content
  taskSplit = ' '.join(message.split()[1:-1])
  dueToSplit = ' '.join(message.split()[-1:])

  sql = "UPDATE todolist SET due_to = %s WHERE todo = %s and user_id = %s"
  value = (dueToSplit, taskSplit, author_id)

  cursor.execute(sql, value)
```
# - Strukturierte Datentypen
Strukturierte Datentypen wurden verwendet, um Datenbankabfragen zu verarbeiten und die Ergebnisse zu strukturieren:

```Python
for row in rows:
    value_todo = row["todo"]
    value_due_to = row["due_to"]

```
