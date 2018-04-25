import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import random

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name="MMGamer.eu"))

@bot.command(pass_context=True)
async def help(ctx):
	#Help categorys coming soon
	if False:
		pass
	else:
		embed=discord.Embed(title="Help", description="```diff \n - !help <category/command> - helps you with stuff \n - !warn <user> <reason> - warn those spammy idiots \n - !ping - check the bot latency \n - !kick <user> - kick ennoying people \n - !embed - tests a embed \n - !delete <amount> - clear spam \n - !info <user> - gets info about a user \n```", color=0x66009D)
		await bot.say(embed=embed)

@bot.command(pass_context=True)
async def gimi(ctx, rank):
	role = discord.utils.get(ctx.message.server.roles, name=rank)
	await bot.add_roles(ctx.message.author, role)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! xSSS")
    print ("user has pinged")
@bot.command(pass_context = True)
async def ban(ctx, member: discord.Member):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '397745647723216898':
        try:
            await bot.ban(member)
            await bot.say("Succesfully issued a ban!")
        except discord.errors.Forbidden:
            await bot.say("To low perms!")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
	embed=discord.Embed(title="Stats for {}".format(user.name), description="Show {} stats".format(user.name), color=0x66009D)
	embed.add_field(name="Name: ", value=user.name, inline=False)
	embed.add_field(name="ID: ", value=user.id, inline=False)
	embed.add_field(name="Status: ", value=user.status, inline=False)
	embed.add_field(name="Top role: ", value=user.top_role, inline=False)
	embed.add_field(name="Joined at: ", value=user.joined_at, inline=False)
	await bot.say(embed=embed)



@bot.command(pass_context=True)
async def warn(ctx, userName: discord.Member, reason: str):
    if "Staff" in [role.name for role in ctx.message.author.roles] or ctx.message.author.server_permissions.administrator:
        embed = discord.Embed(title="Warned", description="{} You have been warned for **{}**".format(userName.mention, reason), color=0x66009D)
        embed.set_thumbnail(url=userName.avatar_url)
        embed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)
	await bot.send_message(userName, embed=embed)
    else:
        await bot.say("{} :x: You are not allowed to use this command!".format(ctx.message.author.mention))
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def delete(ctx, number):
    msgs = []
    number = int(number)
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        msgs.append(x)
    await bot.delete_messages(msgs)
    embed = discord.Embed(title=f"{number} messages deleted", description="Wow, somebody's been spamming", color=0x66009D)
    test = await bot.say(embed=embed)
    await asyncio.sleep(10)
    await bot.delete_message(test)

@bot.command(pass_context = True)
async def kick(ctx, member: discord.Member):
	if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '397745647723216898':
		try:
			await bot.kick(member)
			await bot.say("Succesfully kicked ur nice friend!")
		except discord.errors.Forbidden:
			await bot.say("To low perms!")
	else:
		await bot.say("You dont have perms")
@bot.command(pass_context=True)
async def embed(ctx):
    embed = discord.Embed(title="test", description="my name jeff", color=0x00ff00)
    embed.set_footer(text="this is a footer")
    embed.set_author(name="Will Ryan of DAGames")
    embed.add_field(name="This is a field", value="no it isn't", inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ball(ctx, question):
	await bot.say(random.choice(["NO", "Ofc", "What do u think", "Hmmm", "Yeh"]))

@bot.event
async def on_message(message):
	await bot.process_commands(message)
bot.run("NDM4MDM1ODc2MTAzMzIzNjY2.DcC0VQ.uTHGo5qwIXgs6-Ng4vMELDZshuk")
