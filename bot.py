import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re
import os

client  = discord.Client()



@client.event
async def on_ready():
  print('We have logged in as {0.user}.'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('£hello'):
    await message.channel.send('Hello! :joy:')
  elif message.content.startswith('£father'):
    await message.channel.send('My Father is <@421989746508693516> <:Broondoon:423155569407426563>')
  elif message.content.startswith('£ourjoy'):
    await message.channel.send(':b::b::b::b::b::b::b::b::joy::b::b::b::b::b::b:\n:b::b::b::b::b::joy::joy::b::joy::joy::b::b::b::b::b:\n:b::b::b::b::joy::joy::joy::b::b::joy::joy::b::b::b::b:\n:b::b::b::joy::joy::joy::joy::b::b::b::joy::joy::b::b::b:\n:b::b::joy::joy::joy::joy::b::b::b::b::joy::joy::joy::b::b:\n:b::joy::joy::joy::joy::joy::joy::b::b::b::b::joy::joy::b::b:\n:b::b::joy::joy::b::joy::joy::joy::b::b::b::joy::joy::joy::b:\n:b::b::b::b::b::b::joy::joy::joy::b::b::b::joy::joy::b:\n:b::b::b::b::b::b::b::joy::joy::joy::b::joy::joy::joy::b:\n:b::b::b::b::joy::b::b::b::joy::joy::joy::joy::joy::b::b:\n:b::b::b::joy::joy::joy::b::b::b::joy::joy::joy::b::b::b:\n:b::joy::joy::joy::b::joy::joy::joy::joy::joy::joy::joy::joy::b::b:\n:b::joy::joy::b::b::b::joy::joy::joy::b::b::joy::joy::b::b:')
  elif message.content.startswith('£cock'):
    await message.channel.send('Cock :pensive:')
  elif message.content.startswith('£owner'):
    await message.channel.send('The owner of this server is <@251481886663114754> <:monkaW:422797034312040459>')
  elif message.content.startswith('£help'):
    await message.channel.send('Current commands include: \n£help\n£owner\n£father\n£ourjoy\n£hello')


client.run(os.getenv(Nzk3MjQ0NTI1MDQ2MjY3OTM0.X_jp0g.1C_gJZ9lRP5tJRQyb_MzTLL--jI))