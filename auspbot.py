import discord
from discord.ext import commands
import datetime 
import csv
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
try: 
    with open('log.csv', 'r') as file_in:
        dictReader = csv.DictReader(file_in)
        for line in dictReader:
            if int(line['user_id']) not in allStreakDict:
                allStreakDict[int(line['user_id'])] = {}
            timestamp = line['timestamp'].split()
            date = timestamp[0].split('-')
            timeofDay = timestamp[1].split(':')
            allStreakDict[int(line['user_id'])][int(line['attempt_number'])] = (line['attempt_duration'], datetime.datetime(int(date[0]), int(date[1]), int(date[2]), int(timeofDay[0]), int(timeofDay[1]), int(float(timeofDay[2])//1)), int(line['total_seconds']))
except: 
    pass

def time_parse(diffObject):
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
                timeStr = f'{hours} hours, {minutes} minutes, and {seconds} seconds.'
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
    if ctx.author.id not in list(allStreakDict.keys()):
        
        allStreakDict[ctx.author.id] = {}
        allStreakDict[ctx.author.id][1] = ('No time', datetime.datetime.now(), 0)
        embed = discord.Embed(
            description="First time, eh? Hopefully it\'ll be a while before I see you.",
            color=discord.Colour.blurple(), # Pycord provides a class with default colors you can choose from
        )

        await ctx.respond(embed = embed)
    else:
        inputKey = list(allStreakDict[ctx.author.id].keys())[-1] + 1
        diffObject = datetime.datetime.now() - allStreakDict[ctx.author.id][inputKey-1][1]
        timeStr = time_parse(diffObject)
        embed = discord.Embed(
            description=f'Ah, sorry to hear that. You went for {timeStr}',
            color=discord.Colour.blurple(), # Pycord provides a class with default colors you can choose from
        )
        await ctx.respond(embed=embed)
        allStreakDict[ctx.author.id][inputKey] = (timeStr, datetime.datetime.now(), diffObject.seconds)
        
    with open('log.csv', 'w') as file_out:
        writer = csv.writer(file_out)
        writer.writerow(['user_id', 'attempt_number', 'attempt_duration', 'timestamp', 'total_seconds'])
        for userid in allStreakDict:
            for attempt in allStreakDict[userid]:
                writer.writerow([userid, attempt, allStreakDict[userid][attempt][0], allStreakDict[userid][attempt][1], allStreakDict[userid][attempt][2]])
            
@gameBot.slash_command(
  name="viewallmine",
  guild_ids=[929836210644463718]
)
async def viewallmine(ctx):    
    message = ''
    with open('log.csv', 'r') as file_in:
        dict = csv.DictReader(file_in)
        for line in dict: 
            if int(line['user_id']) == ctx.author.id:
                date = line['timestamp'].split()[0]
                if int(line['attempt_number']) == 1:
                    message += f'First attempt: started on {date}.\n\n' 
                else:
                    message += f'Attempt {line['attempt_number']}: Had a length of {line['attempt_duration'][:-1]} and ended on {date}.\n\n'
    embed = discord.Embed(
        title=f'{ctx.author}: All attempts',
        description=f'{message}',
        color=discord.Colour.blurple(), # Pycord provides a class with default colors you can choose from
    )
    await ctx.respond(embed=embed)
    
        
@gameBot.slash_command(
  name="longestattempt",
  guild_ids=[929836210644463718]
)
async def longestattempt(ctx):    
    max = 1 #Index by attempt number later
    for attempt in allStreakDict[ctx.author.id]:
        if allStreakDict[ctx.author.id][attempt][2] > allStreakDict[ctx.author.id][max][2]:
            max = attempt
    length = allStreakDict[ctx.author.id][max][0][:-1] #Cuts off the period at the end
    date = f'{allStreakDict[ctx.author.id][max][1].month}-{allStreakDict[ctx.author.id][max][1].day}-{allStreakDict[ctx.author.id][max][1].year}'
            
            
    embed = discord.Embed(
        title=f'{ctx.author}\'s Longest attempt:',
        description=f'Your longest attempt had a duration of {length} that ended on {date}',
        color=discord.Colour.blurple(), # Pycord provides a class with default colors you can choose from
    )
    await ctx.respond(embed=embed)

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
                    
    
