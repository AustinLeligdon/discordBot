import discord
import asyncio
from datetime import datetime
import messages
from os import environ
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
        embed = discord.Embed(title="Enjoy the kitty", color=0x00ff00)
        #link# http://thecatapi.com/api/images/get
        embed.set_image(*, 'http://random.cat/i/1219.jpg')

        await client.send_message(message.channel, embed=embed)

#!countdown -Print how many days are left until HackISU 2018
    if message.content.startswith('!countdown'):
        #Get the times and compute the difference
        now = datetime.today()
        hackerTime = datetime(2017, 12, 25, 17) #2018, 3, 23, 17)
        diff = hackerTime - now
        testMessage = ''

        #Print hours to go if it's the same day
        if(diff.days == 0):
            hours = divmod(diff.seconds, 3600)[0]
            timeMessage = 'There are {} hours until HackISU 2018!'.format(hours)
        #IF the event has passed
        elif(diff.days < 0):
            timeMessage = 'It\'s happening!'
        #Print number of days to go if appropriate
        else:
            timeMessage = 'There are {} days until HackISU 2018!'.format(diff.days)

        #send the message to the channel
        await client.send_message(message.channel, timeMessage)

#!help -Print out the possible commands for the bot
    elif message.content.startswith('!help'):
        await client.send_message(message.channel, messages.Help)

#!info -Display the info for HackISU
    elif message.content.startswith('!info'):
        await client.send_message(message.channel, messages.Info)

#!social -Display the links for HackISU's social media platforms
    elif message.content.startswith('!social'):
        await client.send_message(message.channel, messages.Social)
    
#!test -A test command for the bot
    elif message.content.startswith('!test'):
        await client.send_message(message.channel, messages.Test)

#Run locally
#client.run(secret.Token)

#Run on Heroku. Defined under Settings->Config Vars
client.run(environ.get('BOT_TOKEN'))