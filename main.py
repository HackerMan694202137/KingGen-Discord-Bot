from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import requests
import re

load_dotenv()
TOKEN = os.getenv("TOKEN") # make a .env file next to this main.py file, edit it and fill in: TOKEN=YourDiscordBotTokenWithoutThisCharacter"

params = {
    "key": "key"
}

bot = commands.Bot(command_prefix="!")

@bot.command(name='generate')
async def generate(ctx):
    response = requests.get("https://kinggen.info/api/v2/alt", params=params)
    print(response.content)
    email = re.findall("email\":\"(.*?)\"", str(response.content)); print(email)
    password = re.findall("password\":\"(.*?)\"", str(response.content)); print(password)
    emailstring = ''.join(email)
    passwordstring = ''.join(password)
    embed = discord.Embed(title="Generated an alt:", description=f"{emailstring}:{passwordstring}")
    await ctx.send(embed=embed)

bot.run(TOKEN)
