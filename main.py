
import os
import discord
import requests
import json
import random
from jesusWords import jesus
from keep_alive import keep_alive

my_secret = os.environ['token']
client = discord.Client()

#keywords to trigger jesus quotes
god = ["omg","OMG",'god',"God","hey","la","9","annoying","faster","play","onz","tonight","when","holy"]

#get inspirational quotes from API
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = "'"+json_data[0]['q']+"'" + " -" + json_data[0]['a']
  return(quote)

# Function that runs at startup to indicate running
@client.event
async def on_ready():
  print("Hello! {0.user}".format(client))

# function for sending messages
@client.event
async def on_message(message):
  # if message is sent by the bots or me , ignore
  if message.author == client.user or str(message.author.id) == '399208016861331466'or str(message.author.id) == '855724856259248139':
    return
    
  # event priority
  # 1. if msg contains best, prints @Zhang is the best
  # 2. if msg contains jesus triggers, send jesus facts
  # 3. send inspiration shit
  if "best" in message.content:
    user = '<@399208016861331466>'
    await message.channel.send('%s is the best ' % user)
  elif any(word in message.content for word in god):
      n = random.randrange(len(jesus))
      await message.channel.send(message.author.mention + jesus[n])
  else:
      await message.channel.send(message.author.mention + get_quote())

keep_alive()
client.run(my_secret)










