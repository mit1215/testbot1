import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Login As：', client.user)
    game = discord.Game('lol')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "test" or message.content == "Test":
        await message.channel.send('Hi')

    if message.content.startswith('!'):
      tmp = message.content.split(" ",2)
      if len(tmp) == 1:
        await message.channel.send("?")
      else:
        await message.channel.send(tmp[1])

client.run("MTA0MDgxMTI2ODMyMTMxMjc5MQ.GzAwLA.Z__h2dNTXz3073TsgAZBoB8p0p0v3aJU9Y5uXY")
#在Token位放你的Token
