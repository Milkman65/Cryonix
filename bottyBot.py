import os
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import datetime

bot = commands.Bot(command_prefix = "?")

@bot.event
async def on_command_error(ctx, error):
    print("Command error")

#dic for on_message anti-spam    
dic = {}

#not working
async def dic_iterater():

    while not bot.is_closed:
        for i in dic:
            dic[i] -= 1
        print("sleeping")
        await asyncio.sleep(5)




@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return
    if message.author in dic:
        dic[message.author] += 1
        print("incremented, value is {}".format(dic[message.author]))
    else:
        dic[message.author] = 0
        print("intialized dic")
    

   
    

@bot.event
async def on_ready():
    print("Ready to go")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Online (?)"))

@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
    await ctx.channel.send("purging {} messages.".format(amount))
    await asyncio.sleep(3)
    await ctx.message.delete()
    deleted = await ctx.channel.purge(limit=amount)

@bot.command()
async def avatar(ctx, member: discord.Member):
    av = member.avatar_url
    embed=discord.Embed(title="Avatar", color=0x42f4dc)
    embed.set_image(url=av)
    await ctx.channel.send(embed=embed)
    
    

    
    
    
#not working
bot.loop.create_task(dic_iterater())

bot.run("Token")

