# start.py

import discord
from discord.ext import commands

import json
import random
import asyncio
import os
import sys
from dispander import dispand
import asyncio

from lib.instant import instant




class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.joiner = False
        self.mems = {}


    @commands.Cog.listener()
    async def on_ready(self):
        print('Wolf had started')

    @commands.Cog.listener()
    async def on_message(self, message):
        await dispand(message)

    @commands.command()
    async def ready(self,ctx):
        for chan in ctx.guild.channels:
            await chan.delete()

        all_role = ctx.guild.roles
        channel = await ctx.guild.create_text_channel("welcome")
        for rol in all_role:
            try:
                await rol.delete()
            except:
                a = "a"

        category = await ctx.guild.create_category(name="総合")
        await category.create_text_channel("総合チャット")
        voice = await category.create_voice_channel("総合チャット")
        await voice.edit(user_limit=99)

    @commands.command()
    async def start(self,ctx):
        self.joiner = 0
        self.mems = {}
        await ctx.send("開始を確認...\n参加希望の方は、`/join` と入力してください。")
        self.joiner = True
        edit = await ctx.send("開始まで10秒")
        for i in range(10):
            num = 10 - i
            await edit.edit(content=f"開始まで{num}秒")
            await asyncio.sleep(0.9)
        self.joiner = False
        await edit.delete()
        await ctx.send("参加者が決定しました。")
        print(self.mems)
        # if len(self.mems) <= 2:
        #     await ctx.send("参加を希望したのが2名以下だったため、開始できません。\n停止します...")
        #     return
        # txt = "```\n"
        # for name in self.mems.values():
        #     txt += f"・{name}\n"
        # await ctx.send(f"{txt}```")
        cel = self
        await instant.wolf(cel,ctx)
        self.jobs = instant.job(cel)

    @commands.command()
    async def join(self,ctx):
        if self.joiner == False:
            return
        if ctx.author.id in self.mems:
            return
        self.mems[ctx.author.id] = ctx.author.name
        await ctx.message.add_reaction("⭕")



# 人狼２
# 市民３
# 占い師１
# 霊媒師１
# 狩人１
# 狂人１














































def setup(bot):
    bot.add_cog(Game(bot))
