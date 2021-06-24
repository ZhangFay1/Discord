
import os
import discord
import requests
import json
import random
from jesusWords import jesus
from keep_alive import keep_alive

my_secret = os.environ['token']
client = discord.Client()
god = ["omg","OMG",'god',"God","hey","la","9","annoying","faster","play","onz","tonight","when","holy"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = "'"+json_data[0]['q']+"'" + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print("Hello! {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if "best" in message.content:
    user = '<@399208016861331466>'
    await message.channel.send('%s is the best ' % user)
  elif any(word in message.content for word in god):
    if str(message.author.id) == '399208016861331466'or str(message.author.id) == '855724856259248139':
      return
    else:
      n = random.randrange(len(jesus))
      await message.channel.send(message.author.mention + jesus[n])
  else:
    if str(message.author.id) == '399208016861331466'or str(message.author.id) == '855724856259248139':
      return
    else:
      await message.channel.send(message.author.mention + get_quote())

keep_alive()
client.run(my_secret)










