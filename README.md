# BotNeuner

### Yet another Twitch chatbot

It's a chatbot, it's going to do chatbot things.

Realistically, this is starting as me goofing around learning more Python and creating a chat bot because I wanted to.
It most likely will never go live and is just a project to goof around in. Leaving the repo public to A) share it and B)
to teach myself to be a good person and not store my API keys in the script like a lazy piece of shit.

## Requirements

- Python 3 (Currently developing in Python 3.7.2)
- [Twitchio](https://github.com/TwitchIO/TwitchIO)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

I'm also using a `.env` file in the root directory to store environment variables instead of storing them in the OS.
This is why we import python-dotenv. You will either need to create one yourself with the following variables in it or
`EXPORT` / `SET` them in your OS.

Delete lines 4 and 10 if you're going to store the environment variables in OS instead of using the `.env` file.

We need to set these variables:

```
TMI_TOKEN=<generate a token at https://twitchapps.com/tmi/>
TWITCH_CLIENT_ID=<create an app on TwitchDev and use the client ID here>
BOT_NAME=<name of your bot account>
COMMAND_PREFIX=!
TWITCH_ACTIVE_CHANNEL=<name of the channel to join as the bot>
```

## Roadmap

- Spotify integration
- Channel points integration
- OBS integration
- _Who the fuck knows what?_