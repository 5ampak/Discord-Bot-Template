# Main Bot File (bot.py)
import os
import discord
from discord import app_commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('DISCORD_GUILD'))

# Create the bot client and command tree
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    print(f'Slash commands synced to the guild: {GUILD_ID}')
    await setup_commands()

# Load command modules
async def setup_commands():

    from commands.hello         import setup as setup_hello
    
    await setup_hello       (tree, GUILD_ID)

    await tree.sync(guild=discord.Object(id=GUILD_ID)) 
    print("Commands registered and synced")

# Run the bot with your token
client.run(TOKEN)
