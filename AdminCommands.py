import discord

from discord.ext import commands

class AdminCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def kick(self, ctx, member:discord.Member):
	    if not member:
	        await ctx.send('Please specify a member!')
	        return
	    await member.kick()
	    await ctx.send(f'{member.mention} was kicked from the Wizarding World!')

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def ban(self, ctx, member: discord.Member):
		if not member:
			await ctx.send('Please specify a member!')
			return
		await member.ban()
		await ctx.send(f'The Ban Hammer has struck {member.mention}!')

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def unban(self, ctx, *, member):
	    banned_users = await ctx.guild.bans()
	    member_name, member_discriminator = member.split('#')

	    for ban_entry in banned_users:
	        user = ban_entry.user

	        if (user.name, user.discriminator) == (member_name, member_discriminator):
	            await ctx.guild.unban(user)
	            await ctx.send(f'{user.name}#{user.discriminator} is now unbanned!')


	@commands.command()
	@commands.has_permissions(administrator=True)
	async def clear(self, ctx, amount: int):
	    await ctx.channel.purge(limit=amount + 1)
	    mes = f"Deleted {amount} messages"
	    message = await ctx.send(mes)
	    await asyncio.sleep(2)
	    await ctx.channel.purge(limit=1)

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def info(self, ctx, *, member: discord.Member):
	    fmt = '{0} joined on {0.joined_at} and has {1} roles.'
	    await ctx.send(fmt.format(member, len(member.roles)))

	@info.error
	async def info_error(self, ctx, error):
	    if isinstance(error, commands.BadArgument):
	        await ctx.send('I could not find that member...')




def setup(bot):
	bot.add_cog(AdminCommands(bot))