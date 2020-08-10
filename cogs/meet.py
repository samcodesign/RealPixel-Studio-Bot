import discord
from discord.ext import commands


class Meet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meeting(self, ctx):
        embed = discord.Embed(
            title='RPS Metting 3 AT 9PM',
            description='for the our next meeting,we have to agree on a storyline for the game',
            colour=discord.Colour.blurple()
        )
        embed.set_footer(text='By Sam & Moh')
        embed.set_author(name='RPS Bot', icon_url='https://cdn.discordapp.com/attachments/734563166775935016/737464407629627492/Artboard_18.png')
        embed.add_field(name='Storyline Rec', value='-2 sided character -About Cyberpunk+DARK+Superpowers -algerian theme(if possible) after voting for the best storyline,\
                                                    we start developing the ideas and arranging them in a perfect scenario', inline=False)
        embed.add_field(name='Adding', value='make sure to make your storyline clean for the reader and be ready to answer the questions asked by the team members', inline=True)
        embed.add_field(name='NEWS', value='Make sure to welcome our new artist xD', inline= False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Meet(bot))
