import mysql.connector
import discord
from discord.ext import commands

from token import *

# important, gives bot permissions to do something
intents = discord.Intents.default()
intents.message_content = True
intents.members = True 
client = discord.Client(intents=intents)

# prefix
client = commands.Bot(command_prefix= '.', intents=intents)

# connect to database
database = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "discordbot"
)

cursor = database.cursor(dictionary=True)

# info in console
@client.event
async def on_ready():
  print("Ready to use")
  print("____________")

# says hello
@client.command()
async def hello(ctx):
  await ctx.send("Hello")

# says goodbye
@client.command()
async def goodbye(ctx):
  await ctx.send("Adios")

# welcomes member
@client.event
async def on_member_join(member):
  channel_id = 1202990831959543880

  channel = client.get_channel(channel_id)

  await channel.send(f"Welcome, {member}")

# Help
@client.command()
async def info(ctx):
  await ctx.send('''
1. Use ".todo " to write your tasks.
2. Use ".due (Task) (Due)" to add a due to the task.
3. Use ".list" to return all tasks.
4. Use ".removedue (task)" to remove the due from the task.
5. Use ".remove (task)" to delete a specifc task.
6. Use ".removeall" to clear the entire list.
                 ''')

# Adds tasks to a database bound to the users ID
# splitting is used to prevent the command to be also entered in the database
@client.command()
async def todo(ctx):
  message = ctx.message.content
  messageSplit = ' '.join(message.split()[1:])

  sql = "INSERT INTO todolist (todo, user_id) VALUES (%s, %s)"
  value = (messageSplit, ctx.author.id)

  cursor.execute(sql, value)

  database.commit()

# Due to
@client.command()
async def due(ctx):
  author_id = ctx.author.id

  message = ctx.message.content
  taskSplit = ' '.join(message.split()[1:2])
  dueToSplit = ' '.join(message.split()[2:])

  sql = "UPDATE todolist SET due_to = %s WHERE todo = %s and user_id = %s"
  value = (dueToSplit, taskSplit, author_id)

  cursor.execute(sql, value)

  database.commit()

# lists all of the todos from the database bound to ID
@client.command()
async def list(ctx):
  author_id = ctx.author.id

  sql = "SELECT todo, due_to from todolist where user_id = %s"
  value = (author_id,)

  cursor.execute(sql, value)

  rows = cursor.fetchall()
  for row in rows:
    value_todo = row["todo"]
    value_due_to = row["due_to"]

    if(value_due_to != ""):
      await ctx.send(f'* "{value_todo}" is due to "{value_due_to}"')
    else:
      await ctx.send(f'* {value_todo}')

# Clear todo list bound to ID
@client.command()
async def removeall(ctx):
  author_id = ctx.author.id

  sql = "DELETE FROM todolist WHERE user_id = %s"
  value = (author_id,)
    
  cursor.execute(sql, value)

  database.commit()

  await ctx.send("Cleared the List.")

# Remove only one from todo list
@client.command()
async def remove(ctx):
  toDelete = ctx.message.content
  toDeleteSplit = ' '.join(toDelete.split()[1:])

  sql = "DELETE FROM todolist WHERE todo = %s"
  value = (toDeleteSplit,)

  cursor.execute(sql, value)

  database.commit()

  await ctx.send(f'Removed "{toDeleteSplit}" from the list.')   

#Remove Due
@client.command()
async def removedue(ctx):
  toDeleteDue = ctx.message.content
  toDeleteDueSplit = ' '.join(toDeleteDue.split()[1:])

  sql = "UPDATE todolist SET due_to = NULL WHERE todo = %s"
  value = (toDeleteDueSplit,)

  cursor.execute(sql, value)

  database.commit()

  await ctx.send(f'Removed due from "{toDeleteDueSplit}".')   

client.run('MTIwMjk4NjgyMDM1MTE2NDQxNg.GEbJCG.S3gZ9C2Y8TdRlRUcbPFOI5msZR7HkpqApaH3zk')