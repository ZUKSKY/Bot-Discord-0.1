import discord
from discord.ext import commands
from myserver import server_on

TOKEN = " "  # ganti/isi dengan token bot anda

bot = commands.Bot(command_prefix='*')


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle,
                              activity=discord.Activity(
                                  type=discord.ActivityType.watching,
                                  name="GAS LOGIN SERVER"))
    print('Bot {} telah online'.format(bot.user))


@bot.command()
async def hello(ctx):
    await ctx.send('I SEE U , {}! '.format(ctx.author.name.title()))

server_on()
bot.run(TOKEN)