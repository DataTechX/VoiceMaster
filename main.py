import discord
from discord.ext import commands
import traceback
import sys

bot = commands.Bot(command_prefix="+") 

token = 'ODU3MjM5Mjc3NzQ2NjUxMTg2.YNMsSg.OBpSt03paSS-qE0ghIBwdcLpCiE'

initial_extensions = ['cogs.voice']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
bot.run(token)
