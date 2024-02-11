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
intents.message_content = True
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
  print("##############################################")
  print("# The bot is now deployed and ready for use. #")
  print("##############################################")

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
@client.slash_command(guild_ids=[SERVER_ID], description="Our bot will greet you because he's nice :)")
async def hello(interaction: Interaction):
  member = interaction.user.mention
  await interaction.response.send_message(f"Hello, {member}! I am a bot.")

@client.slash_command(guild_ids=[SERVER_ID], description="Our bot will be sad because you leave him :(")
async def bye(interaction: Interaction):
  member = interaction.user.mention
  await interaction.response.send_message(f"Why are you leaving me, {member}? :(")

@client.slash_command(guild_ids=[SERVER_ID], description="Do you need help? You shall receive it.")
async def info(interaction: Interaction):
  await interaction.response.send_message('''
1. Use "/todo" to add a new item to your ToDo-list.
2. Use "/list" to list all items in your ToDo-list.
3. Use "/due" to add a due-date to an existing item in your ToDo-list.
4. Use "/removedue" to remove a due date from a specific item.
5. Use "/remove" to remove an item from your ToDo-list.
6. Use "/removeall" to clear your ToDo-list.
                 ''')

# Adds tasks to a database bound to the user's ID
# splitting is used to prevent the command to be also entered in the database
@client.slash_command(guild_ids=[SERVER_ID], description="Use this command to add a new item to your ToDo-List.")
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

# Due to
@client.slash_command(name="due", description="Use this command to set a due date for an existing item in your ToDo-List.")
async def due(ctx, *, task_and_due_to: str):
  author_id = ctx.user.id

  message = task_and_due_to
  taskSplit = ' '.join(message.split()[:-1])
  dueToSplit = message.split()[-1]

  sql = "UPDATE todolist SET due_to = %s WHERE todo = %s and user_id = %s"
  value = (dueToSplit, taskSplit, author_id)

  cursor.execute(sql, value)
  database.commit()

  await ctx.send("Due date set successfully.")

# List all of the todos from the database bound to ID
@client.slash_command(name="list", description="Use this command to list all of the items in your ToDo-List.")
async def list(ctx):
  author_id = ctx.user.id

  sql = "SELECT todo, due_to from todolist where user_id = %s"
  value = (author_id,)

  cursor.execute(sql, value)

  rows = cursor.fetchall()
  
  if not rows:
    await ctx.send("Congratulations, there are no items in your list!")
  else:
    todos_message = "Your todos:\n"
    for row in rows:
      value_todo = row["todo"]
      value_due_to = row["due_to"]

      if value_due_to != "":
        todos_message += f'* "{value_todo}" is due to "{value_due_to}"\n'
      else:
        todos_message += f'* {value_todo}\n'

    await ctx.send(todos_message)

# Clear todo list bound to ID
@client.slash_command(name="removeall", description="Use this command to clear your ToDo-List.")
async def removeall(ctx):
  author_id = ctx.user.id

  sql = "DELETE FROM todolist WHERE user_id = %s"
  value = (author_id,)
    
  cursor.execute(sql, value)

  database.commit()

  await ctx.send("All your ToDos have been removed from the list.")

# Remove only one from todo list
@client.slash_command(name="remove", description="Use this command to remove a specific entry from your ToDo-List.")
async def remove(ctx, *, todo_item: str):
  toDeleteSplit = todo_item

  sql = "DELETE FROM todolist WHERE todo = %s"
  value = (toDeleteSplit,)

  cursor.execute(sql, value)

  database.commit()

  await ctx.send(f'Removed "{toDeleteSplit}" from the list.')   

# Remove Due
@client.slash_command(name="removedue", description="Use this command to remove a due date for a specific item in your ToDo-List.")
async def removedue(ctx, *, todo_item: str):
  toDeleteDueSplit = todo_item

  sql = "UPDATE todolist SET due_to = NULL WHERE todo = %s"
  value = (toDeleteDueSplit,)

  cursor.execute(sql, value)

  database.commit()

  await ctx.send(f'Removed due from "{toDeleteDueSplit}".')

client.run(DISCORD_TOKEN)