import discord

TOKEN = 'OTYwNTE4MzkwMTk4NDUyMjY0.YkrmdQ.a00OWTuo87KN2c1Tye0_s8WGoo0'

client = discord.Client()

@client.event
async def on_ready():
    print('kp')

@client.event
async def on_message(message):

    if message.author.bot:
        return
    if message.content == '!nae':
        await message.channel.send("https://cdn.discordapp.com/attachments/603123201928855552/959143328258080828/407BD401-0C12-4642-B23A-9DF548B6F220.jpg")
    if message.content == '!hk':
        await message.channel.send("https://cdn.discordapp.com/attachments/603123201928855552/959152855548297287/DAE403F5-8773-4DCE-B9A6-C7318368CCC5.jpg")
    if message.content == '!ikiri':
        await message.channel.send("https://cdn.discordapp.com/attachments/603123201928855552/959144455368212570/5BA63EF3-96B7-4268-86B6-336158B99219.jpg")

client.run(TOKEN)
