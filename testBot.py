import discord
import asyncio
from datetime import datetime
import messages
import os
#To get local token
#import secret

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------')

@client.event
async def on_message(message):
    if message.content.startswith('!help'):
        #Print out the possible commands for the bot
        await client.send_message(message.channel, '\n'.join(messages.Help))
        print('help requested')
    
    elif message.content.startswith('!test'):
        await client.send_message(message.channel, messages.Test)

    elif message.content.startswith('!countdown'):
        now = datetime.today()
        hackerTime = datetime(2017, 12, 25, 17)
        diff = hackerTime - now
        time = ''

        if(diff.days == 0):
            hours = divmod(diff.seconds, 3600)[0]
            time = 'There are ' + str(hours) + ' hours until HackISU 2018!'
        elif(diff.days < 0):
            time = 'It\'s happening!'
        else:
            time = 'There are ' + str(diff.days) + ' days until HackISU 2018!'

        await client.send_message(message.channel, time)

#Run locally
#client.run(secret.Token)

#Run on Heroku. Defined under Settings->Config Vars
client.run(os.environ.get('BOT_TOKEN', None))