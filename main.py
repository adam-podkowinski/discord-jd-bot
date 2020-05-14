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
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == 'general':
            await channel.send(f'''Welcome to the server {member.mention}''')


@client.event
async def on_message(message):
    id = client.get_guild(704264027999567934)
    channels = ['commands']
    valid_users = ['JdMan#9101']

    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find('!hello') != -1 and message:
            await message.channel.send('Hi')
        elif message.content == '!users':
            await message.channel.send(f'''Number of Members: {id.member_count}''')
    else:
        print(
            f'''User: {message.author} tried to do command {message.content}, in channel {message.channel}''')

print('Running client...')
client.run(token)
