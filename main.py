import os
import discord
from sendMama import get_mama
from keep_alive import keep_alive

my_secret = os.environ['token']
client = discord.Client()
zhang_id = '399208016861331466'
groovy_id = '234395307759108106'

# Function that runs at startup to indicate running
@client.event
async def on_ready():
  print("Hello! {0.user}".format(client))

# function for sending messages
@client.event
async def on_message(message):
  # if message is sent by the bots or me , ignore
  if message.author == client.user or str(message.author.id) == zhang_id or str(message.author.id) == groovy_id:
    return

  if "best" in message.content:
    user = '<@'+zhang_id+'>'
    await message.channel.send('%s is the best ' % user)
  else:
      await message.channel.send(message.author.mention + get_mama())

keep_alive()
client.run(my_secret)

 # code which allows me to test program
  # if message.author == client.user or str(message.author.id) == '855724856259248139':
  #   return













