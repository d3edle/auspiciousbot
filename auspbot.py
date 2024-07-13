import discord
from discord.ext import commands
import responses
import datetime 
import time
import json

global allStreakDict
allStreakDict = {}
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
description = 'a bot for playing \"the game\". Congrats, you just lost! :) '

gameBot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    description=description,
    intents=intents,
)

def time_parse(diffObject):
    # print(diffObject.days)
    # print(diffObject.weeks)
    weeks = diffObject.days // 7 
    days = diffObject.days % 7
    hours = diffObject.seconds // 3600
    minutes = diffObject.seconds % 3600 // 60
    seconds = diffObject.seconds % 3600 % 60
    if weeks == 0:
        if days == 0:
            if hours == 0:
                timeStr = f'{minutes} minutes and {seconds} seconds.'
            else:
                timestr = f'{hours} hours, {minutes} minutes, and {seconds} seconds.'
        else:
            timeStr = f'{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.'
    else:
        timeStr = f'{weeks} weeks, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.'   
    return timeStr

@gameBot.slash_command(
  name="lost",
  guild_ids=[929836210644463718]
)
async def lost(ctx): 
    # await ctx.respond("Ah, sorry to hear that.")
    if ctx.author.id not in allStreakDict:
        allStreakDict[ctx.author.id] = {}
        allStreakDict[ctx.author.id][1] = datetime.datetime.now()

        await ctx.respond("First time, eh? Hopefully it\'ll be a while before I see you.")
    else:
        inputKey = list(allStreakDict[ctx.author.id].keys())[-1] + 1
        allStreakDict[ctx.author.id][inputKey] = datetime.datetime.now()
        diffObject = datetime.datetime.now() - allStreakDict[ctx.author.id][inputKey-1]
        
        timeStr = time_parse(diffObject)
        await ctx.respond(f'Ah, sorry to hear that. You went for {timeStr}')
        
    # with open('Log.csv', 'w') as file_out:
        


with open('config.json', 'r') as cfg:
# Deserialize the JSON data (essentially turning it into a Python dictionary object so we can use it in our code) 
    data = json.load(cfg) 
gameBot.run(data["token"])  

#not able to take multiple, needs to be hosted somewhere
# import os
#rhi,monday, 4:30pm
#rhi,1/5/24, 2pm
# async def send_message(message, user_message, guilds, is_private):
#     # try:
#         # if 
#     for guild in guilds: 
#         if guild.name == 'King DeedleP\'s server':
            # await message.channel.send(f'{message.author.mention} set a reminder to do {acc_mesage} at {timeofday}')


            # text_log = await guild.fetch_channel(1247378604321538129)    
            # textLogMsg = f'{message.author.mention} / {message.author} set up a reminder to {acc_mesage}'
            # await text_log.send(textLogMsg)

            # if seconds > 18000:
            #     sleeptime = seconds-18000
            #     time.sleep(sleeptime)
            #     seconds -= sleeptime
            #     await message.author.send(f'{message.author.mention} Hey, 5 hours until you need to do {acc_mesage}...remember, it\'s at {timeofday}')

            # if seconds > 7200:
            #     sleeptime = seconds-7200 
            #     time.sleep(sleeptime)
            #     seconds -= sleeptime
            #     await message.author.send(f'{message.author.mention} Hey, 2 hours until you need to do {acc_mesage}...remember, it\'s at {timeofday}')

            # if seconds > 3600:
            #     sleeptime = seconds-3600
            #     time.sleep(sleeptime)
            #     seconds -= sleeptime
            #     await message.author.send(f'{message.author.mention} Hey, 1 hour until you need to do {acc_mesage}...remember, it\'s at {timeofday}')

            # if seconds > 300:
            #     sleeptime = seconds-300
            #     time.sleep(sleeptime)
            #     seconds -= sleeptime
            #     await message.author.send(f'{message.author.mention} Hey, 5 minutes until you need to do {acc_mesage}...remember, it\'s at {timeofday}')
            # if seconds > 60:
            #     sleeptime = seconds-60
            #     time.sleep(sleeptime)
            #     seconds -= sleeptime
            #     await message.author.send(f'{message.author.mention} Hey, one minute until you need to do {acc_mesage}...remember, it\'s at {timeofday}')

            # if seconds > 5:
            #     sleeptime = seconds-5
            #     time.sleep(sleeptime)
            #     seconds -= sleeptime
            #     for i in range(20):
            #         await message.author.send(f'{message.author.mention} Hey, it\'s happening RIGHT NOW! You need to do {acc_mesage.upper()} right NOW at {timeofday}!!!!')
            #         time.sleep(.5)
        
    # except Exception as e:
    #     print(e, 1)


# def run_discord_bot():
    # gameBot = commands.Bot()

    # try:
    # gameBot = commands.bot()
    # for guild in gameBot.guilds: 
    #     if guild.name == 'King DeedleP\'s server':
    #         print('hi')
    

    # intents=discord.Intents.default()
    # intents.message_content = True
    # client = discord.Client(intents=intents)
    
    
    # except Exception as e:
    #     print(e, 1)       


    # @client.event
    # async def on_ready():
    #     print(f'{client.user} is now running!')

    # @client.event
    # async def on_message(message):
    #     if message.author != client.user: #client.user is the FUCKING BOT bruh
    #         username = str(message.author)
    #         user_message = str(message.content).lower()
    #         channel = str(message.channel)
    #         split = user_message.split()
    #         if split[0][0] == 'r':
    #             user_message = user_message[1:]
    #             await send_message(message, user_message, client.guilds, is_private=True)
                    
    
