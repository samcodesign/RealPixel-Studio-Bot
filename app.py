import random
import asyncio
import discord
import os
from itertools import cycle
from discord.ext import commands, tasks

greeting = ['Hey', 'Ola', 'Hi', 'Marhaba', 'Huh']
bot = commands.Bot(command_prefix=['RPS ', 'rps '])
token = "NzM0ODA5NTk3Mjg1NDk4OTYw.XxYVHw.h14EbUJjCUomfiogpK21ytfNKmM"


# status to choose from
status = cycle(['The Game Of Life', 'Be optimist',
                'Life sounds crazy', 'Developing a game...', 'Fuck Covid'])
# function decorator



@bot.event
async def on_ready():
    # when bot becomes ready, status is changed to online, activity,
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(next(status)))
    # starts status change
    change_status.start()
    print(random.choice(greeting), ', Bot is ready Captain.')


# Create task // Loop that updates status of bot every 10 sec
@tasks.loop(seconds=15)
async def change_status():
    # setting activity to discord.Game object, using cycle status passed in as games name
    await bot.change_presence(activity=discord.Game(next(status)))


# Cogs part
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


# 8ball game
@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain',
                 'Without a doubt',
                 'You may rely on it',
                 'Yes definitely',
                 'It is decidedly so',
                 'As I see it, yes',
                 'Most likely',
                 'Yes',
                 'Outlook good',
                 'Signs point to yes',
                 'Reply hazy try again',
                 'Better not tell you now',
                 'Ask again later',
                 'Cannot predict now',
                 'Concentrate and ask again',
                 'Don’t count on it',
                 'Outlook not so good',
                 'My sources say no',
                 'Very doubtful',
                 'My reply is no']

    if ctx.author.id == 465636226729508896:
        if ctx.message.content == 'rps 8ball ana babak?':
            await ctx.send("Wsh baba cv?")
    else:
        await ctx.send("Hum...")
        await asyncio.sleep(3)
        await ctx.send(f'{random.choice(responses)}')


# deleting messages
@bot.command()
async def clear(ctx, amount: int):
    # taking context, accessing channel, on channel we are calling purge method, limit is amount
    await ctx.channel.purge(limit=amount+1)


@bot.event
async def daddy(ctx):
    if ctx.author.id == 465636226729508896:
        if ctx.message.content == 'rps ana babak?':
            await ctx.send("Wsh baba cv?")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid Command Used.')


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an amount of messages to delete.')


# Run application
bot.run(token)
