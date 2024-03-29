# Importing required dependencies
import os
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import requests
import json
from dotenv import load_dotenv

# Storing tokens in variables
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
JOKE = os.getenv('JOKE_TOKEN')
CHANNEL_GENERAL = int(os.getenv('CHANNEL_GENERAL'))

# Some setup for making this stuff work
intents = nextcord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
  print("The bot is now ready for use!")

@client.command()
async def hello(ctx):
  await ctx.send("Hello, I am a bot")
@client.command()
async def truth(ctx):
  await ctx.send("Existence is nothing but pain.")

testServerId = 1200881581234081904

# Slash commands
@client.slash_command(guild_ids=[testServerId])
async def test(interaction: Interaction):
  await interaction.response.send_message("Hello, I am a bot.")

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

client.run(DISCORD_TOKEN)