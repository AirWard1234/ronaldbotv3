import asyncio
import discord
import json
import os
import random
import youtube_dl

from discord.ext import commands
from discord.utils import get

os.chdir('C:\\Users\\sandr\\Desktop\\Ronald Bot')

client = commands.Bot(command_prefix = '?')
client.remove_command('help')

@client.event
async def on_ready():
	print('Ron is ready!')

async def ch_pr():
	await client.wait_until_ready()
	stats = [f'on {len(client.guilds)} servers! | ?help','a game with the mods! | ?help']
	while not client.is_closed():

		stats2 = random.choice(stats)
		await client.change_presence(activity = discord.Game(name = stats2))

		await asyncio.sleep(10)

@client.command()
async def help(ctx):
	embed = discord.Embed(


			colour = discord.Colour.orange()
	)
	embed.add_field(name = "FUN COMMANDS👾🧙", value = '8ball(ask a question after the command), slap(command + @), coinflip, dadjoke, potterhead(gives you a random Harry Potter fact!), wyr(would you rather), lenny, minecraftseed')
	embed.add_field(name = "MODERATION COMMANDS🤓", value = 'ban, unban, clear (+ amount), info (get info from a person in the server!), kick, upvote')
	embed.add_field(name= 'INVITE RONALD', value="add Ronald to join the Wizarding World: https://discordbotlist.com/bots/ronald")
	embed.set_author(name="Help! my prefix is '?'")

	await ctx.author.send(embed=embed)


extensions = ['AdminCommands.py', 'FunCommands.py', 'CommandEvents.py']

if __name__ == '__main__':	
	for ext in extensions:
			client.load_extension(ext)

client.loop.create_task(ch_pr())
client.run('Nzk0MzU0MzI1MjQ1MjYzOTAz.X-5mHQ.ORo4FbWA2oDSrN-gx2DP8eZf43Q')
