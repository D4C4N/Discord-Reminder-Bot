import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
  print("The bot is now ready for use!")

@client.command()
async def hello(ctx):
  await ctx.send("Hello, I am a bot")
@client.command()
async def truth(ctx):
  await ctx.send("Existence is nothing but pain.")

client.run(TOKEN)