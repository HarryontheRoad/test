import asyncio
import discord
import bla

players = {}
d = discord.Client()
bananenbrot = "277083383425794058"
vollkornbrot = "360859154249678858"
admins = ["277083383425794058", "360859154249678858"]


@d.event
async def on_ready():
    print('Logged in as')
    print(d.user.name)
    print(d.user.id)
    print('------')
    await d.change_presence(game=discord.Game(name='Bester Discord der Welt'))


@d.event
async def on_message(message):
    if message.content.startswith(bla.prefix + 'test'):
        counter = 0
        tmp = await d.send_message(message.channel, 'Calculating messages...')
        async for log in d.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await d.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith(bla.prefix + 'sleep'):
        await asyncio.sleep(5)
        await d.send_message(message.channel, 'Done sleeping')
    if message.content.startswith(bla.prefix + 'text'):
        await d.send_message(message.channel, 'hallo halloi ')
        d.change_nickname()
    if message.content.startswith(bla.prefix + 'game'):
        print('geht 1')
        if message.author.id == bananenbrot:
            game = message.content[6:]
            await d.change_presence(game=discord.Game(name=game))
            await  d.send_message(message.channel, 'Ich habe mein Spiel zu ' + game + ' geändert')
        else:
            d.send_message(message.channel, '----------nicht genug rechte----------')

        if message.author.id == vollkornbrot:
            game = message.content[6:]
            await d.change_presence(game=discord.Game(name=game))
            await  d.send_message(message.channel, 'Ich habe mein Spiel zu ' + game + ' geändert')
        else:
            d.send_message(message.channel, '----------nicht genug rechte----------')
    if message.content.startswith(bla.prefix + 'restart'):
        await d.change_presence(game=discord.Game(name='--restart--'))
        d.close()
        print('restart')
    if message.content.startswith(bla.prefix + 'help'):
       await d.send_message(message.channel, 'Es gibt die Befehle:' )
       await d.send_message(message.channel, '! test' + bla.descriptionTest)
       await d.send_message(message.channel, '! sleep' + bla.descriptionSleep)
       await d.send_message(message.channel, '! text' + bla.descriptionText)
       await d.send_message(message.channel, '! game' + bla.descriptionGame)
       await d.send_message(message.channel, '! restart' + bla.descriptionRestart)
       await d.send_message(message.channel, '! help' + bla.descriptionHelp)
       await d.send_message(message.channel, '! bjoern' + bla.descriptionBjoern)
    if message.content.startswith(bla.prefix + 'bjoern'):
        if message.author.id == bananenbrot:
            d.send_message(message.channel, 'Hallo Björn')
        if message.author.id == vollkornbrot:
            d.send_message(message.channel, 'Hallo Björn')
    if message.content.startswith(bla.prefix + 'join'):
            try:
                channel = message.author.voice.voice_channel
                await d.join_voice_channel(channel)
            except discord.errors.InvalidArgument:
                await d.send_message(message.channel, 'Du musst in einem Channel sein...')
                print('...')
            except Exception as error:
                await d.send_message(message.channel, 'Der Fehler ist: ```{error}```'.format(error=error))
    if message.content.startswith(bla.prefix + 'quit'):
            try:
                voice_client = d.voice_client_in(message.server)
                await  voice_client.disconnect()
            except AttributeError:
                await d.send_message(message.channel, 'Ich bin in keinem Channel...')
            except Exception as fehler:
                await d.send_message(message.channel, 'Der Fehler ist: ```{fehler1}```'.format(fehler1=fehler))
    if message.content.startswith(bla.prefix + 'play'):
        bla.liedURL3 = message.content[6:]
        try:
            if message.content[6:].startswith(bla.liedText1):
                try:
                    channel = message.author.voice.voice_channel
                    voice = await d.join_voice_channel(channel)
                    player = await voice.create_ytdl_player(bla.liedURL1)
                    d.send_message(message.channel, "Wird geladen...")
                    players[message.server.id] = player
                    player.start()
                    d.send_message(message.channel, "Wurde geladen!")
                except discord.Err
            elif message.content[6:].startswith(bla.liedText2):
                try:
                    channel = message.author.voice.voice_channel
                    voice = await d.join_voice_channel(channel)
                    player = await voice.create_ytdl_player(bla.liedURL2)
                    d.send_message(message.channel, "Wird geladen...")
                    players[message.server.id] = player
                    player.start()
                    d.send_message(message.channel, "Wurde geladen!")
                except Exception as error:
                    await d.send_message(message.channel, 'Der Fehler ist: ```{fehler}```'.format(fehler=error))
            elif message.content[6:].startswith(bla.liedText3):
                try:
                    channel = message.author.voice.voice_channel
                    voice = await d.join_voice_channel(channel)
                    player = await voice.create_ytdl_player(bla.liedURL3)
                    d.send_message(message.channel, "Wird geladen...")
                    players[message.server.id] = player
                    player.start()
                    d.send_message(message.channel, "Wurde geladen!")
                except Exception as error:
                    await d.send_message(message.channel, 'Der Fehler ist: ```{fehler}```'.format(fehler=error))
        except:
            pass
    if message.content.startswith(bla.prefix + 'pause'):
        try:
            players[message.server.id].pause()
        except Exception as error:
            await d.send_message(message.channel, 'Der Fehler ist: ```{fehler}```'.format(fehler=error))
    if message.content.startswith(bla.prefix + 'resume'):
        try:
            players[message.server.id].resume()
        except Exception as error:
            await d.send_message(message.channel, 'Der Fehler ist: ```{fehler}```'.format(fehler=error))
    if message.content.startswith(bla.prefix + 'kick'):
        member = message.content[6:]

        member.User.id

        await d.kick(member)

@d.event
async def on_member_join(member):
    chennel = bla.channel
    await d.send_message(discord.message.channel, "hi")


d.run(bla.token)

#
# await d.send_message(message.channel, 'Der Fehler ist: ```{fehler}```'.format(fehler=error))


#