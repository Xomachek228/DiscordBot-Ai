import discord, os, requests
from discord.ext import commands
from discord.ext.commands import bot
from Config import TOKEN
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def chek(ctx):
    if ctx.message.attachments:
        for i in ctx.message.attachments:
            file_name = i.filename
            await i.save(f"./images/{file_name}")
            await ctx.send(get_class(f"./images/{file_name}"))
    else:
        await ctx.send("Вы забыли добавить вложение")

bot.run(TOKEN)