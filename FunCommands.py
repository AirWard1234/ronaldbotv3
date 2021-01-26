import discord
import random
import praw

from discord.ext import commands

reddit = praw.Reddit(client_id = 'z8qy_4sX1sutIQ',
					 client_secret = 'jsgB4knVxJm5BYjbspH4s8ebt5QYGQ',
					 username = 'AirWardx',
					 password = 'Sandrika12',
					 user_agent = 'praw')

subreddit = reddit.subreddit('dankmemes')

top = subreddit.top(limit = 100)

for submission in top:
	print(submission.title)

class FunCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def meme(self, ctx):
		subreddit = reddit.subreddit('dankmemes')
		all_subs = []
		top = subreddit.top(limit = 100)
		all_subs.append(submission)
		random_sub = random.choice(all_subs)
		name = random_sub.title
		url = random_sub.url

		embed = discord.Embed(
				title = name , 
				colour = embed.Colour.orange()
			)
		embed.set_image(name = f'{name}', value = f'{url}')

		await ctx.send(embed=embed)

	@commands.command()
	async def wyr(self, ctx):
		q = ['🟦 Be Batman?  or \n🟥 Be Superman?',
			 '🟦 Have more money?  or \n🟥 Have more time?',
			 '🟦 Have the ability to speak to animals  ?  or \n🟥 Have the ability to speak every language?',
			 '🟦 Explore the Deep Space?  or \n🟥 Explore the Deep Ocean',
			 '🟦 Be too cold?  or \n🟥 Be too hot?',
			 '🟦 Be Harry Potter?  or \n🟥 Be Percy Jackson?',
			 '🟦 Work by yourself?  or \n🟥 Work with others?',
			 '🟦 Win the lottery?  or \n🟥 Live twice as long?',
			 '🟦 Lose your vision?  or \n🟥 Lose your hearing?',
			 '🟦 Work longer hours a day but for less days?  or \n🟥 Work shorter days but more days?',
			 '🟦 Go yo to the movies alone?  or \n🟥 Go to the dinner alone?',
			 '🟦 Put a stop on all the wars?  or \n🟥 Put a stop to world hunger?',
			 '🟦 X-Ray vision?  or \n🟥 Magnified hearing?',
			 '🟦 Have a cook?  or \n🟥 Have a maid?',
			 '🟦 Have a desk job?  or \n🟥 Have a outdoor job?',
			 '🟦 Have Rambo on your side?  or \n🟥 Have The Terminator on your side?',
			 '🟦 Be too busy?  or \n🟥 Be too bored?',
			 '🟦 Have a rewind button in real life?  or \n🟥 Have a pause button in real life?',
			 '🟦 Have have nosy neighbors?  or \n🟥 Have noisy neighbors?',
			 '🟦 Hear the good news first?  or \n🟥 Hear the bad news first?',
			 '🟦 Live with constant Winter?  or \n🟥 Live with constant Summer?',
			 '🟦 Be a pro gamer?  or \n🟥 Be a pro athlete?',
			 '🟦 Be a little late?  or \n🟥 Be too early?',
			 '🟦 Have a unlimited gift certificate to a clothing store?  or \n🟥 Have a unlimited gift certificate to a restaurant?',
			 '🟦 Date someone you met online?  or \n🟥 Go on a blind date?',
			 '🟦 Have a Summer vacation?  or \n🟥 Have a Winter vacation?',
			 '🟦 Be poor and work at a job you love?  or \n🟥 Be rich an work at a job you hate  ?',
			 '🟦 Have a sexy companion, but dumb as hell?  or \n🟥 Have a ugly companion, but super smart?',
			 '🟦 Have the best house but worst neighbourhood?  or \n🟥 Have the worst house but the best neighbourhood?',
			 '🟦 Be rich but live 400 years ago?  or \n🟥 Be poor but live in the present?',
			 '🟦 Go with out TV for the rest of your life?  or \n🟥 Go with out junk food for the rest of your life?',
			 '🟦 Be known for your intelligence?  or \n🟥 Be known for your good looks?',
			 '🟦 Never mentally age?  or \n🟥 Never physically age?',
			 '🟦 Change your eye colour?  or \n🟥 Change your hair colour?',
			 '🟦 Have a family with 12 children?  or \n🟥 Never be able to have children?',
			 '🟦 Be a one-hit wonder songwriter?  or \n🟥 Be a one-hit wonder book writer?']
		

		embed = discord.Embed(
				colour = discord.Colour.orange()
			)
		embed.add_field(name = 'Would You Rather!', value = f'{random.choice(q)}')

		message = await ctx.send(embed=embed)
		await message.add_reaction('🟦')
		await message.add_reaction('🟥')

	@commands.command(aliases=['8ball'])
	async def _8ball(self, ctx, *, question):
	    responses = ['It is certain.',
	                'It is decidedly so.',
	                'Without a doubt.',
	                'Yes - definitely.',
	                'You may rely on it.',
	                'As I see it, yes.',
	                'Most likely.',
	                'Outlook good.',
	                'Yes.',
	                'Signs point to yes.',
	                'Reply hazy, try again.',
	                'Ask again later.',
	                'Better not tell you now.',
	                'Cannot predict now.',
	                'Concentrate and ask again.',
	                'Do not count on it',
	                'My reply is no.',
	                'My sources say no.',
	                'Outlook not so good.',
	                'Very doubtful.']

	    await ctx.send(f'Question: {question} \nAnswer: {random.choice(responses)}')

	@commands.command()
	async def slap(self, ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
	    slapped = ", ".join(x.name for x in members)
	    await ctx.send('{} just got slapped for {}'.format(slapped, reason))

	@commands.command()
	async def invite(self, ctx):
		await member.send('So you are a fan of the Wizarding World, might as well add Ronald to your server to start up some fun! https://discord.com/api/oauth2/authorize?client_id=794354325245263903&permissions=8&scope=bot')

	@commands.command()
	async def coinflip(self, ctx):
		results = ['Heads',
	 			   'Tales']

		embed = discord.Embed(
				colour = discord.Colour.orange()
		)

		embed.add_field(name = "Coin Flip ($)", value = f'{random.choice(results)}')

		await ctx.send(embed=embed)

	@commands.command(aliases=['dadjokes'])
	async def dadjoke(self, ctx):
		jokes = ['I am so good at sleeping I can do it with my eyes closed!',
				 'What do you call a bee that lives in America? A USB.',
				 "What do you call a duck that gets all A's? A wise quacker.",
				 'Why are elevator jokes so classic and good? They work on many levels.',
				 "What kind of noise does a witch’s vehicle make? Brrrroooom, brrroooom.",
				 'I dreamt about drowning in an ocean made of orange soda.It took me a minute to realize it was just Fanta-sea.',
				 'Why did the m&m go to school? Because it wanted to be a Smartie!',
				 'Past, present, and future walked into a bar.... It was tense.',
				 'What did one pirate say to the other when he beat him at chess?<>Checkmatey.',
				 'I burned 2000 calories today.I left my food in the oven for too long.',
				 'I startled my next-door neighbor with my new electric power tool. <>I had to calm him down by saying “Don’t worry, this is just a drill!”',
				 'I broke my arm in two places. <>My doctor told me to stop going to those places.',
				 'I quit my job at the coffee shop the other day. <>It was just the same old grind over and over.',
				 'I never buy anything that has Velcro with it...<>it’s a total rip-off.',
				 'I used to work at a soft drink can crushing company...<>it was soda pressing.',
				 'I wondered why the frisbee kept on getting bigger. <>Then it hit me.',
				 'I was going to tell you a fighting joke...<>but I forgot the punch line.',
				 'What is the most groundbreaking invention of all time? <>The shovel. ',
				 'I’m starting my new job at a restaurant next week. <>I can’t wait.',
				 'I visited a weight loss website...<>they told me I have to have cookies disabled.',
				 'Did you hear about the famous Italian chef that recently died? <>He pasta way.',
				 'Broken guitar for sale<>no strings attached.',
				 'I could never be a plumber<>it’s too hard watching your life’s work go down the drain.',
				 'I cut my finger slicing cheese the other day...<>but I think I may have grater problems than that.',
				 'What kind of music do astronauts listen to?<>Neptunes.',
				 'Rest in peace, boiled water. <>You will be mist.',
				 'What is the only concert in the world that costs 45 cents? <>50 Cent, featuring Nickelback.',
				 'It’s not a dad bod<> it’s a father figure.',
				 'My wife recently went on a tropical food diet and now our house is full of this stuff. <>It’s enough to make a mango crazy.',
				 'What do you call Santa’s little helpers? <>Subordinate clauses.',
				 'Want to hear a construction joke? <>Sorry, I’m still working on it.',
				 'What’s the difference between a hippo and a zippo? <>One is extremely big and heavy, and the other is a little lighter.',
				 'I burnt my Hawaiian pizza today in the oven, <>I should have cooked it on aloha temperature.',
				 'Anyone can be buried when they die<>but if you want to be cremated then you have to urn it.',
				 'Where did Captain Hook get his hook? <>From the second-hand store.',
				 'I am such a good singer that people always ask me to sing solo<>solo that they can’t hear me. ',
				 'I am such a good singer that people ask me to sing tenor<>tenor twelve miles away.',
				 'Occasionally to relax I just like to tuck my knees into my chest and lean forward.<> That’s just how I roll.',
				 'What did the glass of wine say to the glass of beer? Nothing. <>They barley knew each other.',
				 'I’ve never trusted stairs. <>They are always up to something.',
				 'Why did Shakespeare’s wife leave him? <>She got sick of all the drama.',
				 'I just bought a dictionary but all of the pages are blank. <>I have no words to describe how mad I am.',
				 'If you want to get a job at the moisturizer factory... <>you’re going to have to apply daily.',
				 'I don’t know what’s going to happen next year. <>It’s probably because I don’t have 2020 vision.',
				 'Want to hear a joke about going to the bathroom? <>Urine for a treat.',
				 'I couldn’t figure out how to use the seat belt. <>Then it just clicked.',
				 'I got an email the other day teaching me how to read maps backwards<>turns out it was just spam.',
				 'I am reading a book about anti-gravity.<> It is impossible to put down!',
				 'You are American when you go into the bathroom, and you are American when you come out, but do you know what you are while you are in there?<> European.',
				 'Did you know the first French fries were not actually cooked in France?<> They were cooked in Greece.',
				 'Want to hear a joke about a piece of paper? Never mind... <>its tearable.']

		embed = discord.Embed(
				colour = discord.Colour.orange()
			)

		embed.set_author(name = f'{random.choice(jokes)}')

		await ctx.send(embed=embed)

	@commands.command()
	async def potterhead(self, ctx):
		facts = ['JK Rowling and Harry Potter share the same birthday!',
				 'She invented the names of the Hogwarts houses on the back of a barf bag.',
				 "Dementors were based on Rowling's struggle with depression after her mom died.",
				 "The Wizarding World's plants come from a real book!",
				 "They were going to name the American version of Philosopher's Stone as Harry Potter and the School of magic!",
				 'Arthur Weasly was supposed to die!',
				 'To keep Deathly Hallows from being from leaking early, Bloomsbury gave it codenames!',
				 "The director of 'Harry Potter and the Prisoner of Azkaban' made the trio write an essay about their character!",
				 'Some of the effects in Harry Potter were not computer generated.',
				 "There could've been an official Harry Potter Musical",
				 'Dumbledore was gay.',
				 'Rowling acknowledged that a Harry/Hermione pairing might have worked.',
				 "Back in the day, the Malfoy's hung out with rich muggles",
				 'Stephen King thought Dolores Umbridge was a great villian.',
				 'Colors have deeper meaning in the HP world. Red represents goodness, which is why Gryffindor’s robes are red and the Weasleys have red hair. Green is associated with negative events, like when Harry saw a flash of green when his parents died.',
				 'The actors were not allowed to play contact sports because they weren’t safe, so they only played golf during their free time.',
				 'The HP books were the first children’s books on the New York Bestseller list since Charlotte’s Web in 1952.',
				 'Rowling has said that if she were a teacher at Hogwarts, she would teach Charms, and if she had a job, she would write spell books.',
				 " Fred and George Weasley, perpetual jokers, were born on April Fools’ Day.",
				 "The name Voldemort comes from French words that mean 'flight of death.'",
				 "Shirley Henderson, who played 14-year-old Moaning Myrtle, was 36 when filming began.",
				 "Harry’s eyes are described as green in the books, but Radcliffe’s eyes are not green. They tried green contacts, but Radcliffe had a bad reaction to them and couldn’t use them.",
				 "Both Radcliffe and Grint admitted to having crushes on Watson when filming early movies.",
				 "In the second film, there’s a scene where Harry explains he’s missing a sock. For that scene, Radcliffe had to shave one leg.",
				 "The feasts of food in Harry Potter and the Sorcerer’s Stone was all real food… but it wasn’t really enjoyed, since it spoiled quickly because of hot lights on set.",
				 "Rowling spent the first five years writing Harry Potter just setting up rules on what the characters could and couldn’t do.",
				 " In Prisoner of Azkaban, Professor Trelawney refused to sit at a table with 12 other characters because she would be the 13th and the first one to get up after that would die. In Order of the Phoenix, 13 members of the order are sitting and Sirius was the first one to stand up."]

		embed = discord.Embed(
				colour = discord.Colour.orange()
			)

		embed.set_author(name = f'{random.choice(facts)}')
		await ctx.send(embed=embed)

	@commands.command()
	async def upvote(self, ctx):
		embed = discord.Embed(
				colour = discord.Colour.orange()
			)
		embed.add_field(name = 'Upvote Ronald!', value = "Hey I am the developer of Ronald and I'm trying to get him verified please upvote Ronald so more people use him: https://discordbotlist.com/bots/ronald")

		await ctx.send(embed = embed)

	@commands.command()
	async def simprater(self, ctx):
		p = ['10',
			 '20',
			 '30',
			 '40',
			 '50',
			 '60',
			 '70',
			 '80',
			 '90',
			 '100']

		embed = discord.Embed(
				colour = discord.Colour.orange()
			)
		embed.add_field(name = 'Simp Rater (science machine🧪)!', value = f'You are {random.choice(p)}% simp')

		await ctx.send(embed = embed)

	@commands.command()
	async def lenny(self, ctx):
		faces = ["( ͡° ͜ʖ ͡°)",
				 "¯\_(ツ)_/¯",
				 "̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿",
				 "(ง ͠° ͟ل͜ ͡°)ง",
				 "┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻",
				 "(╯°□°）╯︵ ┻━┻",
				 "(☞ﾟヮﾟ)☞ ☜(ﾟヮﾟ☜)",
				 "▄︻̷̿┻̿═━一",
				 "(ノಠ益ಠ)ノ彡┻━┻",
				 "| (• ◡•)| (❍ᴥ❍ʋ)",
				 "(;´༎ຶД༎ຶ`)",
				 "(;´༎ຶД༎ຶ`)",
				 "̿ ̿ ̿'̿'\̵͇̿̿\з=(•_•)=ε/̵͇̿̿/'̿'̿ ̿",
				 "(づ￣ ³￣)づ",
				 "ᕦ(ò_óˇ)ᕤ",
				 "(☞ຈل͜ຈ)☞",
				 "Ƹ̵̡Ӝ̵̨̄Ʒ",
				 "ಠ‿↼",
				 "╚═( ͡° ͜ʖ ͡°) ═╝",
				 "░░░░░░░░░░░░▄▄▄▄░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄\n░░░█░░░░▄▀█▀▀▄░░▀▀▀▄░░░░▐█░░░░░░░░░▄▀█▀▀▄░░░▀█▄\n░░█░░░░▀░▐▌░░▐▌░░░░░▀░░░▐█░░░░░░░░▀░▐▌░░▐▌░░░░█▀\n░▐▌░░░░░░░▀▄▄▀░░░░░░░░░░▐█▄▄░░░░░░░░░▀▄▄▀░░░░░▐▌\n░█░░░░░░░░░░░░░░░░░░░░░░░░░▀█░░░░░░░░░░░░░░░░░░█\n▐█░░░░░░░░░░░░░░░░░░░░░░░░░░█▌░░░░░░░░░░░░░░░░░█\n█░░░░░░░░░░░░░░░░░░░░░░░░░░█▌░░░░░░░░░░░░░░░░░█\n░█░░░░░░░░░░░░░░░░░░░░█▄░░░▄█░░░░░░░░░░░░░░░░░░█\n░▐▌░░░░░░░░░░░░░░░░░░░░▀███▀░░░░░░░░░░░░░░░░░░▐▌\n░░█░░░░░░░░░░░░░░░░░▀▄░░░░░░░░░░▄▀░░░░░░░░░░░░█\n░░░█░░░░░░░░░░░░░░░░░░▀▄▄▄▄▄▄▄▀▀░░░░░░░░░░░░░█﻿﻿",
				 "( ͡° ͜つ ͡°)╭∩╮",
				 "(▀̿̿Ĺ̯̿̿▀̿ ̿)ﾉ ︵ ┻━┻'",
				 "乁(✿ ͡° ͜ʖ ͡°)و",
				 "( ͡°                    ͜ʖ.                       ͡°)﻿",]
		embed = discord.Embed(
				colour = discord.Colour.orange()
			)
		embed.add_field(name = 'Lenny!', value = f'{random.choice(faces)}')
		await ctx.send(embed=embed)

	@commands.command()
	async def minecraftseed(self, ctx):
		seeds = ['-573947210',
				 '2029492581',
				 '1594305760',
				 '2467475923055248755',
				 '3302368487053953130',
				 '1045298416328037846',
				 '87953651674304230',
				 '-5479241985391318616',
				 '2928333153647998182',
				 '166372429861907',
				 '-1989697309261941466',
				 '79634747242878',
				 '-4031664694685636388',
				 '208028093084392',
				 '28407671996037',
				 '1084369785651148524',
				 '-4083076012164728592',
				 '243007488060923',
				 '179821671022351',
				 '158533492472955']

		embed = discord.Embed(
				colour = discord.Colour.orange()
			)
		embed.add_field(name = '1.16.5 MineCraft Seeds', value = f'The seed is: {random.choice(seeds)}')

		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(FunCommands(bot))