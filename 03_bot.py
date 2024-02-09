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


# adds the user-id to the database
@client.command()
async def add(ctx):
  author_id = ctx.author.id

  sql = "INSERT INTO users (ID) VALUES %s"
  values = (author_id,)

  cursor.execute(sql, values)

  database.commit()

# adds the todo to a new table in the same database
# connected to each user through the users ID
# splitting is used to prevent the command to be also entered in the database
@client.command()
async def todo(ctx):
  message = ctx.message.content
  messageSplit = ' '.join(message.split()[1:])

  sql = "INSERT INTO todolist (todo, user_id) VALUES (%s, %s)"
  value = (messageSplit, ctx.author.id)

  cursor.execute(sql, value)

  database.commit()

# lists all of the todos from the database bound to ID
@client.command()
async def list(ctx):
  author_id = ctx.author.id

  sql = "SELECT todo from todolist where user_id = %s"
  value = (author_id,)

  cursor.execute(sql, (value))

  rows = cursor.fetchall()
  for row in rows:
    await ctx.send(row["todo"])

# Clear todo list bound to ID
@client.command()
async def removeall(ctx):
  author_id = ctx.author.id

  sql = "DELETE FROM todolist WHERE user_id = %s"
  value = (author_id,)
    
  cursor.execute(sql, value)

  database.commit()

# Remove only one from todo list
@client.command()
async def remove(ctx):
  toDelete = ctx.message.content
  toDeleteSplit = ' '.join(toDelete.split()[1:])

  sql = "DELETE FROM todolist WHERE todo = %s"
  value = (toDeleteSplit,)

  cursor.execute(sql, value)

  database.commit()   

client.run('MTIwMjk4NjgyMDM1MTE2NDQxNg.GEbJCG.S3gZ9C2Y8TdRlRUcbPFOI5msZR7HkpqApaH3zk')