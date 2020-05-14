import discord


def read_token():
    with open('token.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

client = discord.Client()
client.run(token)
