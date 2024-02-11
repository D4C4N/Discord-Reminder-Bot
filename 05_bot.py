# Importing required dependencies 
import os
from dotenv import load_dotenv
import requests
import json
import mysql.connector
import nextcord
from nextcord import Interaction
from nextcord.ext import commands

# Storing tokens in variables
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
JOKE = os.getenv('JOKE_TOKEN')
CHANNEL_GENERAL = int(os.getenv('CHANNEL_GENERAL'))
SERVER_ID = int(os.getenv('SERVER_ID'))

# Some required setup to make this work
intents = nextcord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intents)

# Establishing database connection
database = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "discordbot"
)

cursor = database.cursor(dictionary=True)

# Console output upon successful bot launch
@client.event
async def on_ready():
  print("The bot is now deployed and ready for use.")

# Message on member join, using a joke API
@client.event
async def on_member_join(member):
  jokeUrl = "https://dad-jokes.p.rapidapi.com/random/joke"

  headers = {
    "X-RapidAPI-Key": JOKE,
    "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
  }

  response = requests.get(jokeUrl, headers=headers)

  channel = client.get_channel(CHANNEL_GENERAL)
  setup = json.loads(response.text)["body"][0]["setup"]
  punchline = json.loads(response.text)["body"][0]["punchline"]
  await channel.send(f"Hello, {member.mention} here is a joke for you:\n{setup} - {punchline}")

#Message on member leave
@client.event
async def on_member_remove(member):
  channel = client.get_channel(CHANNEL_GENERAL)
  await channel.send(f"{member.mention} has left us, we are sad to see them go.")

# Slash commands
@client.slash_command(guild_ids=[SERVER_ID])
async def hello(interaction: Interaction):
  await interaction.response.send_message("Hello, I am a bot.")

@client.slash_command(guild_ids=[SERVER_ID])
async def bye(interaction: Interaction):
  await interaction.response.send_message("Why are you leaving me? :(")

@client.slash_command(guild_ids=[SERVER_ID])
async def info(interaction: Interaction):
  await interaction.response.send_message('''
1. Use ".todo " to write your tasks.
2. Use ".due (Task) (Due)" to add a due to the task.
3. Use ".list" to return all tasks.
4. Use ".removedue (task)" to remove the due from the task.
5. Use ".remove (task)" to delete a specifc task.
6. Use ".removeall" to clear the entire list.
                 ''')

# Adds tasks to a database bound to the user's ID
# splitting is used to prevent the command to be also entered in the database
@client.slash_command(guild_ids=[SERVER_ID])
async def todo(ctx, *, todo_item: str):
  # Extract the todo item from the command
  messageSplit = todo_item

  # Insert the todo item into the database
  sql = "INSERT INTO todolist (todo, user_id) VALUES (%s, %s)"
  value = (messageSplit, ctx.author.id)

  cursor.execute(sql, value)
  database.commit()

  await ctx.send("Todo item added successfully!")

# Due to
@client.slash_command(name="due", description="Set due date for a todo item")
async def due(ctx, *, task_and_due_to: str):
  author_id = ctx.author.id

  message = task_and_due_to
  taskSplit = ' '.join(message.split()[:-1])
  dueToSplit = message.split()[-1]

  sql = "UPDATE todolist SET due_to = %s WHERE todo = %s and user_id = %s"
  value = (dueToSplit, taskSplit, author_id)

  cursor.execute(sql, value)
  database.commit()

  await ctx.send("Due date set successfully.")

# List all of the todos from the database bound to ID
@client.slash_command(name="list", description="List all todos")
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
@client.slash_command(name="removeall", description="Clear todo list")
async def removeall(ctx):
  author_id = ctx.author.id

  sql = "DELETE FROM todolist WHERE user_id = %s"
  value = (author_id,)
    
  cursor.execute(sql, value)

  database.commit()

  await ctx.send("Cleared the List.")

# Remove only one from todo list
@client.slash_command(name="remove", description="Remove a todo item")
async def remove(ctx, *, todo_item: str):
  toDeleteSplit = todo_item

  sql = "DELETE FROM todolist WHERE todo = %s"
  value = (toDeleteSplit,)

  cursor.execute(sql, value)

  database.commit()

  await ctx.send(f'Removed "{toDeleteSplit}" from the list.')   

# Remove Due
@client.slash_command(name="removedue", description="Remove due date from a todo item")
async def removedue(ctx, *, todo_item: str):
  toDeleteDueSplit = todo_item

  sql = "UPDATE todolist SET due_to = NULL WHERE todo = %s"
  value = (toDeleteDueSplit,)

  cursor.execute(sql, value)

  database.commit()

  await ctx.send(f'Removed due from "{toDeleteDueSplit}".')

client.run(DISCORD_TOKEN)