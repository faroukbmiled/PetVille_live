from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import discord
from discord import Interaction, app_commands, ui
from discord.ext import commands
from discord.ext.commands import Bot
from requests import get
import requests
from io import StringIO 
from urllib.request import urlopen
import json
import sys

if TYPE_CHECKING:
    import bot


class Admin(commands.Cog):
    """Error handler"""

    def __init__(self, bot: petville) -> None:
        global thumb, errorgif, logoMsize ,logoSsize, doggif, api_status,\
        api_states
        with open('data/links.json') as links:
            data = json.load(links)
        api_status = data["api_status"]
        api_states = data["api_states"]
        doggif = data["doggif"]
        logoSsize = data["logoSsize"]
        logoMsize = data["logoMsize"]
        errorgif = data["errorgif"]
        thumb = data["thumb"]
        self.bot: petville = bot

    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx: commands.Context, sync_type: Literal['guild', 'global']) -> None:
        """Sync the application commands"""

        async with ctx.typing():
            if sync_type == 'guild':
                self.bot.tree.copy_global_to(guild=ctx.guild)
                await self.bot.tree.sync(guild=ctx.guild)
                await ctx.reply(f"Synced guild !")
                return

            await self.bot.tree.sync()
            await ctx.reply(f"Synced global !")

    @commands.command()
    @commands.is_owner()
    async def unsync(self, ctx: commands.Context, unsync_type: Literal['guild', 'global']) -> None:
        """Unsync the application commands"""

        async with ctx.typing():
            if unsync_type == 'guild':
                self.bot.tree.clear_commands(guild=ctx.guild)
                await self.bot.tree.sync(guild=ctx.guild)
                await ctx.reply(f"Un-Synced guild !")
                return

            self.bot.tree.clear_commands()
            await self.bot.tree.sync()
            await ctx.reply(f"Un-Synced global !")

    @app_commands.command(description='About [ANoX] Ryuk')
    async def ryuk(self, interaction: Interaction) -> None:
        """info about ryuk"""

        embed = discord.Embed(color=0x000000)

        embed.set_image(url="https://cdn.discordapp.com/avatars/346011366747930624/c7fe28d56e899f4955e9e405e6986996.webp?size=256")
        embed.add_field(name="About [ANoX] Ryuk!",value='Server Admin/Clan Founder', inline=False)
        embed.add_field(
            name='Info:',
            value=f"* FPS lover, mainly plays Valorant \n(rank: ASC2)\n"
            "* One of the Founders of 'ANoX Clan' \nand an OG COD player\n"
            "* A Software/Web Dev ,currently studying \nat Holberton School\n",
            inline=False,
        )
        embed.add_field(name="More...",value='* Find more about Ryuk from the links bellow!.', inline=False)
        view = ui.View()
        view.add_item(ui.Button(label='Github', url="https://github.com/faroukbmiled", row=0))
        view.add_item(ui.Button(label='Email', url="https://mail.google.com/mail/u/0/#inbox?compose=CllgCJlFmSRrLHffRzcPGbFZgbdJvswFhKxDSHXmMgrJRfvVMRNMRJZcvQphGxCwwFpkcKVwxdq", row=0))

        await interaction.response.send_message(f"<@{interaction.user.id}> Here:", embed=embed, view=view)

    @app_commands.command(description='list states')
    async def states(self, interaction: Interaction) -> None:
        """info about status"""
        api = api_states
        status = get(api)
        
        if status.status_code != 200:
            
            embed = discord.Embed(color=0xFF0000)
            embed.add_field(name=f"Server Status: [{status.status_code}]",value="Oh no! Server is not responding!", inline=False)
            embed.set_thumbnail(url=thumb)
            embed.set_image(url=errorgif)
            view = ui.View()
            view.add_item(ui.Button(label='API Link', url=api_status, row=0))
            await interaction.response.send_message(f"<@{interaction.user.id}> Here:", embed=embed, view=view) 

        elif len(get(api).json()) == 0:
            embed = discord.Embed(color=0xFF0000)
            embed.add_field(name=f"States: [{status.status_code}]",value="Your Database is empty! ,Please check", inline=False)
            embed.set_image(url=errorgif)
            view = ui.View()
            embed.set_thumbnail(url=logoMsize)
            view.add_item(ui.Button(label='API Link', url=api_status, row=0))
            await interaction.response.send_message(f"<@{interaction.user.id}> Here:", embed=embed, view=view)
            
        else:
            empty = ['\---------------']
            jsonify = get(api).json()
            if status:
                for i in jsonify:
                    empty.append(f'{i["name"]}')
            formated = ('\n* '.join(empty))
            length = len(jsonify)

            embed = discord.Embed(color=0x000000)
            embed.add_field(name=f"States: [{length}]",value=formated, inline=False)
            view = ui.View()
            embed.set_thumbnail(url=thumb)
            view.add_item(ui.Button(label='API Link', url=api_states, row=0))
            await interaction.response.send_message(f"<@{interaction.user.id}> Here:", embed=embed, view=view)

    @app_commands.command(description='status')
    async def status(self, interaction: Interaction) -> None:
        """info about status"""
        status = get(api_status)
        if status.status_code != 200:

            embed = discord.Embed(color=0xFF0000)
            embed.add_field(name=f"Server Status: [{status.status_code}]",value="Oh no! Server is not responding!", inline=False)
            embed.set_thumbnail(url=thumb)
            embed.set_image(url=errorgif)
            view = ui.View()
            view.add_item(ui.Button(label='API Link', url=api_status, row=0))
            await interaction.response.send_message(f"<@{interaction.user.id}> Here:", embed=embed, view=view)
        else:
            ok = status.json().get('status')
            embed = discord.Embed(color=0x00FF00)
            embed.add_field(name=f"Server Status: [{ok}]",
            value=f"Server is up and runing!\n", inline=False)
            embed.set_thumbnail(url=thumb)
            embed.set_image(url=doggif)
            view = ui.View()
            view.add_item(ui.Button(label='API Link', url=api_status, row=0))
            await interaction.response.send_message(f"<@{interaction.user.id}> Here:", embed=embed, view=view)

async def setup(bot: petville) -> None:
    await bot.add_cog(Admin(bot))
