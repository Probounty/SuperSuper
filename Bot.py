import discord
from discord.ext import commands
import time
import random
from random import randint
from random import choice
import json
from discord.ext.commands.cooldowns import BucketType
import typing
from discord.utils import get
import os
import traceback
import sys
import subprocess
import aiohttp
import asyncio




bot = commands.Bot(command_prefix='?', description='This is test')
bot.remove_command('help')

@bot.event
async def on_ready():
    print("bot is online!")







@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(name=f"{len(set(bot.get_all_members()))} | ?Comm ", type=discord.ActivityType.watching), status=discord.Status.do_not_disturb)
    print("Bot is online!")



@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def Twitter(ctx):
    await ctx.send("https://twitter.com/TeamRio40377426")





@bot.command()
async def comm(ctx):
    embed = discord.Embed(title="**__The Perfix Is:?__**" , description= "`Usuall commands`:\n ping\n instagram\n Twitter\n streamers\n`Administrator commands`\n say\n kick\n ban\n unban" , color=0x1b85b1)
    embed.set_footer(text=' כל הזכויות שמורות לקלאן ריוט', icon_url=ctx.bot.user.avatar_url)
    await ctx.send(embed=embed)





@bot.command()
async def sponsor(ctx):
    await ctx.message.delete()
    await ctx.send("https://gamme8.com/")




@bot.command()
async def instagram(ctx):
    await ctx.message.delete()
    await ctx.send("https://www.instagram.com/itsroni_spammm/")


@commands.has_permissions(administrator=True)
@bot.command()
async def say(ctx , *, args):
    embed = discord.Embed(description=args, color=0xc4ffef)
    await ctx.message.delete()
    await ctx.send(embed=embed)


@commands.has_permissions(administrator=True)
@bot.command()
async def kick(ctx, member : discord.Member, *, reason=':x: Error! Missing reason'):
    await member.kick(reason=reason)
   






@commands.has_permissions(administrator=True)
@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)



@commands.has_permissions(administrator=True)
@bot.command()
async def unban(ctx, * , member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user= ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
            return



@bot.command()
async def dis(ctx):
    embed = discord.Embed(title = "**https://discord.gg/BeaVT6K**")
    await ctx.send(embed=embed)






@bot.command()
async def streamers(ctx):
    embed = discord.Embed(title = "Our streamers!", description = "`CABESSA`\n https://www.youtube.com/channel/UCrm8VG7BfQe54_RGR4QBuqQ\n `BenGG`\n https://www.youtube.com/channel/UCl53nIgDbGPmn5uvZhLWTwg\n `STW AVIV`\nhttps://www.youtube.com/channel/UCkqah-yc10KoDcsbDNA_anw\n `RoTeX`\nhttps://www.youtube.com/channel/UCKmSW5yuNhCSl-WOnhZAYIw\n `Amitmit`\nhttps://www.youtube.com/channel/UCXv9aaMIbglclRVkODnjCcA\n `Pitbull`\nhttps://www.youtube.com/channel/UCGgtJEM5ml6bG_ALOK6UQDQ\n `BOBO`\nhttps://www.youtube.com/channel/UCWRRwc9w5MNrLx7DaoG-ONg")
    await ctx.send(embed=embed)



@commands.has_permissions(administrator=True)
@bot.command()
async def avatar(ctx, member: discord.Member = None):
    await ctx.channel.purge(limit=1)
    if not member:
        await ctx.send("Please Metion A Member To Show His/Her Avatar.")
        return
    embed = discord.Embed(
        colour = discord.Color.green()
        )

    embed.set_image(url='{}'.format(member.avatar_url))
    await ctx.send(embed=embed)

        
    










bot.run("NjQ1MzU5MzYyODIyMzczMzc2.XdQ8gA.YxyeZXC_zYC9G9F8AcLdip3EkVM")

