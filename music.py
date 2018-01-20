
import discord

import bla
players = {}

d = discord.Client()

@d.event
async def on_ready():
    print(d.user.name)
    print("==================")
@d.event
async def on_message(message):
    if message.content.startswith('!join'):
            try:
                channel = message.author.voice.voice_channel
                await d.join_voice_channel(channel)
            except discord.errors.InvalidArgument:
                await d.send_message(message.channel, 'Du musst in einem Channel sein...')
                print('...')
            except Exception as error:
                await d.send_message(message.channel, 'Der Fehler ist: ```{error}```'.format(error=error))
    if message.content.startswith('!quit'):
            try:
                voice_client = d.voice_client_in(message.server)
                await  voice_client.disconnect()
            except AttributeError:
                await d.send_message(message.channel, 'Ich bin in keinem Channel...')
            except Exception as fehler:
                await d.send_message(message.channel, 'Der Fehler ist: ```{fehler1}```'.format(fehler1=fehler))
    if message.content.startswith('!play'):
        link = message.content[6:]
        try:
            channel = message.author.voice.voice_channel
            voice = await d.join_voice_channel(channel)
            player = await voice.create_ytdl_player(link)
            d.send_message(message.channel, "Wird geladen...")
            players[message.server.id] = player
            player.start()
            d.send_message(message.channel, "Wurde geladen!")
        except Exception as error:
            await d.send_message(message.channel, 'Der Fehler ist: ```{fehler}```'.format(fehler=error))
    if message.content.startswith('!pause'):
        try:
            players[message.server.id].pause()
        except Exception as error:
            await d.send_message(message.channel, 'Der Fehler ist: ```{fehler}```'.format(fehler=error))
    if message.content.startswith('!resume'):
        try:
            players[message.server.id].resume()
        except Exception as error:
            await d.send_message(message.channel, 'Der Fehler ist: ```{fehler}```'.format(fehler=error))




d.run(bla.token)