import discord

print('Starting...')


def read_token():
    with open('token.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()
print('Read token successfully')

client = discord.Client()


# @client.event
# async def on_member_join(member):
# for channel in member.guild.channels:
# if str(channel) == 'general':
# await channel.send(f'''Welcome to the server {member.mention}''')


@client.event
async def on_message(message):
    if message.content.find('jd') != -1 and message:
        list_mess = message.content.split()
        if len(list_mess) > 1:
            try:
                times = list_mess[list_mess.index('jd') + 1]
                times = int(times)
            except Exception:
                times = 1
        else:
            times = 1
        for _ in range(times):
            await message.channel.send(':regional_indicator_j: :regional_indicator_d:')
            await message.channel.send('''
░░░░░██╗██████╗░
░░░░░██║██╔══██╗
░░░░░██║██║░░██║
██╗░░██║██║░░██║
╚█████╔╝██████╔╝
░╚════╝░╚═════╝░''')

print('Running client...')
client.run(token)
