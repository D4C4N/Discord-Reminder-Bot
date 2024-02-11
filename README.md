# Discord-Reminder-Bot
A discord bot that allows users to set reminders, view reminders and mark reminders as complete.

# Grading Criteria Programmieren T3INF1004
In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.
Alle Kriterien betreffen nur die Projektarbeit. Beweismaterial kommt aus dem Gruppenprojekt.

## FACHKOMPETENZ (40 Punkte)

# Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)
<!-- Siehe Kenntnisse in prozeduraler Programmierung: zutreffendes wählen und beweisen-->

## Variablen Deklaration
```Python
message = ctx.message.content
```

## Verwendung von Dictionaries
```Python
database = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "discordbot"
)
```

## Einsatz von Bibliotheken
```Python
import mysql.connector
import discord
from discord.ext import commands
```

# Sie können die Syntax und Semantik von Python (10)
<!-- Eine Stelle aus ihrem Programmieren wählen auf die sie besonders stolz sind und begründen -->

## Einsatz von for-Schleifen
```Python
  rows = cursor.fetchall()
  for row in rows:
    value_todo = row["todo"]
    value_due_to = row["due_to"]
```

## Einsatz von If und else
```Python
    if(value_due_to != ""):
      await ctx.send(f'* "{value_todo}" is due to "{value_due_to}"')
    else:
      await ctx.send(f'* {value_todo}')
```

## Asynchrones Programmieren

```Python
@client.command()
async def removeall(ctx):
```

# Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)
<!-- Anhand von commits zeigen, wie jeder im Projekt einen Beitrag geleistet hat -->


# Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)
<!-- Eine Stelle aus dem Projekt wählen auf die sie besonders stolz sind und begründen -->

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



## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

# Die Studierenden können ihre Software erläutern und begründen. (5)
<!-- Jeder in der Gruppe: You have helped someone else and taught something to a fellow student (get a support message from one person) -->

# Sie können existierenden Code analysieren und beurteilen. (5)
<!-- Pro Gruppe:You have critiqued another group project. Link to your critique here (another wiki page on your git) and link the project in the critique, use these evaluation criteria to critique the other project. Make sure they get a top grade after making the suggested changes -->
[Critique for the group ToDoListPythonProject](https://github.com/SvenSrc/Programming-Habit/wiki/Critique-for-the-group:-ToDoListPythonProject) 

# Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)
<!-- Which technology did you learn outside of the teacher given input -->
<!-- Did you or your group get help from someone in the classroom (get a support message here from the person who helped you) -->

* Discord-API
* MySQL

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

# - Algorithmenbeschreibung
[RSA-Algorithm](https://github.com/SvenSrc/Programming-Habit/discussions/12)

# - Datentypen

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

# - Kontrollstrukturen
```Python
    if(value_due_to != ""):
      await ctx.send(f'* "{value_todo}" is due to "{value_due_to}"')
    else:
      await ctx.send(f'* {value_todo}')
```
# - Funktionen

```Python
async def removeall(ctx):
  author_id = ctx.author.id

  sql = "DELETE FROM todolist WHERE user_id = %s"
  value = (author_id,)
    
  cursor.execute(sql, value)

  database.commit()

  await ctx.send("Cleared the List.")
```

# - Stringverarbeitung
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


