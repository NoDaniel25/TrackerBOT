import discord
import schedule
import time

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

count = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    curTime = time.localtime()
    current_time = time.strftime("%H:%M:%S", curTime)
    print(current_time)
    count = 0


@client.event
async def on_message(message):
    global count
    if message.author == client.user:
        return

    if message.content.startswith('hi'):
        count += 1
        await message.channel.send('Hello, you have typed ' + str(count) + ' times in the chat')


client.run('MTA3ODc1MTIxNDg2MDI1OTM1OA.Gy9hCN.VPeihamCEW6PmFT89G0v1Oe7RH8ldowaecu9-k')