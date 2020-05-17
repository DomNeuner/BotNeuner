# importing all the things
from twitchio.ext import commands
import os
from dotenv import load_dotenv
from custom_modules import spotify

# var inits go here

# using dotenv to store envvars because it is easier bruh
load_dotenv()

# function to init the bot
bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['TWITCH_CLIENT_ID'],
    nick=os.environ['BOT_NAME'],
    prefix=os.environ['COMMAND_PREFIX'],
    initial_channels=[os.environ['TWITCH_ACTIVE_CHANNEL']]
)

@bot.event
async def event_ready():
    print(f"{os.environ['BOT_NAME']} is online!")
    print("Waiting for commands.")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['TWITCH_ACTIVE_CHANNEL'], f"/me says s'up nerds. I'm online now")

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send(f'pong!')

@bot.command(name='song')
async def ping(ctx):
    current_title, current_artist, current_song_URL = spotify.check()
    await ctx.send(f'The song you can hear is {current_title} by {current_artist}. You can find it on Spotify at {current_song_URL}')

# if we're running, run duh
if __name__ == '__main__':
    bot.run()