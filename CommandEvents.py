import discord
import json
import os

from discord.ext import commands

os.chdir('C:\\Users\\sandr\\Desktop\\Ronald Bot')

class CommandEvents(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_member_join(self, member):
	    with open('users.json', 'r') as f:
	        users = json.load(f)

	    await update_data(users, member)

	    with open('users.json', 'w') as f:
	        json.dump(users, f)

	@commands.Cog.listener()
	async def update_data(self, users, user):
	    if not f'{user.id}' in users:
	        users[f'{user.id}'] = {}
	        users[f'{user.id}']['experience'] = 0
	        users[f'{user.id}']['level'] = 1


	async def on_message(self, message):
	    if message.author.bot == False:
	        with open('users.json', 'r') as f:
	            users = json.load(f)

	        await update_data(users, message.author)
	        await add_experience(users, message.author, 5)
	        await level_up(users, message.author, message)

	        with open('users.json', 'w') as f:
	            json.dump(users, f)
	    await client.process_commands(message)

	async def update_data(self, users, user):
	    if not f'{user.id}' in users:
	        users[f'{user.id}'] = {}
	        users[f'{user.id}']['experience'] = 0
	        users[f'{user.id}']['level'] = 1


	async def add_experience(self, users, user, exp):
	    users[f'{user.id}']['experience'] += exp


	async def level_up(self, users, user, message):
	    experience = users[f'{user.id}']['experience']
	    lvl_start = users[f'{user.id}']['level']
	    lvl_end = int(experience ** (1 / 4))
	    if lvl_start < lvl_end:
	        await message.channel.send(f'BLOODY HELL!{user.mention} has leveled up to level {lvl_end}!')
	        users[f'{user.id}']['level'] = lvl_end

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
	    if isinstance(error, commands.CommandNotFound):
	        await ctx.send('Invalid command used.')


def setup(bot):
	bot.add_cog(CommandEvents(bot))