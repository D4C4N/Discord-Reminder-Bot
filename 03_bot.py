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
client = commands.Bot(command_prefix= '?', intents=intents)

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
    channel = client.get_channel(1202990831959543880)
    await channel.send(f"Welcome, {member}")


# adds the user-id to the database
@client.command()
async def add(ctx):
    cursor.execute(f"INSERT INTO users (ID) VALUES ({ctx.author.id})")

    database.commit()

client.run('Token')