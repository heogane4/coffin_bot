import discord
from discord.ext import commands
from discord.ext import tasks
import logging
import os


bot = commands.Bot(command_prefix='/')
bot.remove_command('help')


@bot.event
async def on_ready():
    print("다음으로 로그인 완료.")
    print(bot.user.name)
    print(bot.user.id)
    print("======================")


@bot.command(aliases=['매장'])
async def kick(ctx, user_name: discord.Member, reason=None):
    await user_name.kick(reason=reason)

    embed=discord.Embed(title=str(user_name), description=" ", color=0xfcdf03)
    embed.set_image(url="https://media1.giphy.com/media/j6ZlX8ghxNFRknObVk/200.gif")
    await ctx.send(embed=embed)
    await ctx.send(str(user_name)+"이(가) 매장 당하였습니다...")

@bot.event
async def on_message(message):
    await bot.process_commands(message)

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
