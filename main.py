import discord

print('Starting...')


def read_token():
    with open('token.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()
print('Read token successfully')

client = discord.Client()


@client.event
async def on_message(message):
    id = client.get_guild(704264027999567934)

    if message.content.find('!hello') != -1 and message:
        await message.channel.send('Hi')
    elif message.content == '!users':
        await message.channel.send(f'''# of Members {id.member.count}''')

print('Running client...')
client.run(token)
