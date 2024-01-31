import discord
from discord import Intents

intents = Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('Natsuki,'):
        # Separa a pergunta da menção à Natsuki
        question = message.content[8:].strip()
        # Cria uma resposta para a pergunta
        response = 'Você perguntou: "{0}"'.format(question)
        await message.channel.send(response)

client.run('') #código do bot (key)
