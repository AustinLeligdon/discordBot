import discord
import asyncio
from datetime import datetime
import messages
from os import environ
import requests
#To get local token
#import secret

client = discord.Client()

#Log the bot into the Discord channel. On success the bot will show as online
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------')

#When a user sends a message in the channel
@client.event
async def on_message(message):
#!cat -send a random image of a cat
    if message.content.startswith('!cat'):
        response = requests.get('http://thecatapi.com/api/images/get', stream=True)
        with open ('cat.png', 'wb') as f:
            f.write(response.raw.read())
        with open('cat.png', 'rb') as f:
            await client.send_file(message.channel, f, filename='cat.png', content='Please, enjoy this cat.')


#!countdown -Print how many days are left until HackISU 2018
    if message.content.startswith('!countdown'):
        #Get the times and compute the difference
        now = datetime.utcnow()
        hackerTime = datetime(2017, 12, 25) #2018, 3, 23, 17)
        diff = hackerTime - now
        testMessage = ''

        #If the event has passed
        if(diff.days < 0):
            timeMessage = 'It\'s happening!'
        #Print number of days to go
        else:
            timeMessage = 'There are {} days until Christmas!'.format(diff.days)

        #send the message to the channel
        await client.send_message(message.channel, timeMessage)

#!help -Print out the possible commands for the bot
    elif message.content.startswith('!help'):
        embed=discord.Embed(color=0x008000)
        embed.add_field(name='Welcome to the Discord Bot. List of commands:', value=messages.Help, inline=False)
        await client.send_message(message.channel, embed=embed)

#!info -Display the info for HackISU
    elif message.content.startswith('!info'):
        embed=discord.Embed(color=0x008000)
        embed.add_field(name='HackISU Spring 2018 Info', value=messages.Info, inline=False)
        await client.send_message(message.channel, embed=embed)

#!social -Display the links for HackISU's social media platforms
    elif message.content.startswith('!social'):
        embed=discord.Embed(color=0x008000)
        embed.add_field(name='Social Media Links', value=messages.Social, inline=False)
        await client.send_message(message.channel, embed=embed)
    
#!test -A test command for the bot
    elif message.content.startswith('!test'):
        await client.send_message(message.channel, messages.Test)

#Run locally
#client.run(secret.Token)

#Run on Heroku. Defined under Settings->Config Vars
client.run(environ.get('BOT_TOKEN'))
