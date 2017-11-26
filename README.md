# discordBot
Testing out making a discord bot for HackISU 2018. After adding features and testing it locally I started hosting it on Heroku 24/7. The bot accepts the following commands:
* !cat        -conjure a random picture of a cat 
* !countdown  -time left until the next hackathon 
* !help       -display the help command 
* !info       -display the info for HackISU 
* !social     -display the links for HackISU's social media platforms 
* !test       -a test command for the bot

### structure
* bot.py       - bot logic
* messages.py  - holds string variables for the bot
* secret.py    - holds the token variable

### built with
* python 3.6
* discord.py
* Heroku
* datetime
* thecatapi.com
