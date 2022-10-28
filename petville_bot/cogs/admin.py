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
        with open('data/links.json') as links:
            data = json.load(links)
        self.web_link = data ["web_link"]
        self.port_link = data ["port_link"]
        self.itsfinegif = data ["itsfinegif"]
        self.api_status = data["api_status"]
        self.api_users = data["api_users"]
        self.doggif = data["doggif"]
        self.logoSsize = data["logoSsize"]
        self.logoMsize = data["logoMsize"]
        self.errorgif = data["errorgif"]
        self.thumb = data["thumb"]
        self.api_token = data["api_token"]
        self.headers = {'Authorization': 'Token 5bd3665cf4eb402a36e4f1945623fa7f0a34134c'}
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

    @app_commands.command(description='About PetVille')
    async def about(self, interaction: Interaction) -> None:
        """info about petville"""

        embed = discord.Embed(color=0x000000)

        embed.set_thumbnail(url=self.logoSsize)
        embed.add_field(name="About PetVille!",value='* Your Pets are in safe Hands!', inline=False)
        embed.add_field(
            name='Info:',
            value=f"* We simply host a platform that offers both\n"
            "a pet sitting service and the sitting job itself",
            inline=False,
        )
        embed.add_field(name="More...",value='* Find more about PetVille from the links bellow!.', inline=False)
        view = ui.View()
        view.add_item(ui.Button(label='Website', url=self.web_link, row=0))
        view.add_item(ui.Button(label='Portfolio', url=self.port_link, row=0))

        await interaction.response.send_message(f"<@{interaction.user.id}> Here:", embed=embed, view=view)

    @app_commands.command(description='list users')
    @app_commands.describe(token="Your token")
    async def users(self, interaction: Interaction, token: str) -> None:
        """info about users"""
        api = self.api_users
        status = requests.get(api, headers=self.headers)
        
        if status.status_code != 200:
            
            embed = discord.Embed(color=0xFF0000)
            embed.add_field(name=f"**Server Status:** [{status.status_code}]",value="**Oh no! Server is not responding!**", inline=False)
            embed.set_thumbnail(url=self.thumb)
            embed.set_image(url=self.errorgif)
            view = ui.View()
            view.add_item(ui.Button(label='API Link', url=self.api_users, row=0))
            await interaction.response.send_message(f"<@{interaction.user.id}> Here:", embed=embed, view=view) 

        elif len(get(api).json()) == 0:
            embed = discord.Embed(color=0xFFA500)
            embed.add_field(name=f"**Server Status** [{status.status_code}]:",value="**Your Database is empty!**", inline=False)
            embed.set_image(url=self.itsfinegif)
            view = ui.View()
            embed.set_thumbnail(url=self.logoMsize)
            view.add_item(ui.Button(label='API Link', url=self.api_users, row=0))
            await interaction.response.send_message(f"<@{interaction.user.id}> Here:", embed=embed, view=view)
            
        else:
            headers = {'Authorization': []}
            headers['Authorization'] = token
            empty = ['\---------------']
            jsonify = requests.get(api, headers=headers).json()
            if status:
                for i in jsonify:
                    empty.append(f'{i["username"]}')
            formated = ('\n* '.join(empty))
            length = len(jsonify)

            embed = discord.Embed(color=0x7ac3e6)
            embed.add_field(name=f"**Users:** [{length}]",value=formated, inline=False)
            view = ui.View()
            embed.set_thumbnail(url=self.logoSsize)
            view.add_item(ui.Button(label='API Link', url=self.api_users, row=0))
            await interaction.response.send_message(f"<@{interaction.user.id}> Here:", embed=embed, view=view)
    @app_commands.command(description='list users')
    @app_commands.describe(token="Your token")
    @app_commands.describe(userid="Your userid")
    async def userid(self, interaction: Interaction, token: str,userid: str ) -> None:
        """info about users"""
        api = self.api_users
        status = requests.get(api, headers=self.headers)
        
        if status.status_code != 200:
            
            embed = discord.Embed(color=0xFF0000)
            embed.add_field(name=f"**Server Status:** [{status.status_code}]",value="**Oh no! Server is not responding!**", inline=False)
            embed.set_thumbnail(url=self.thumb)
            embed.set_image(url=self.errorgif)
            view = ui.View()
            view.add_item(ui.Button(label='API Link', url=self.api_users, row=0))
            await interaction.response.send_message(f"<@{interaction.user.id}> Here:", embed=embed, view=view) 

        elif len(get(api).json()) == 0:
            embed = discord.Embed(color=0xFFA500)
            embed.add_field(name=f"**Server Status** [{status.status_code}]:",value="**Your Database is empty!**", inline=False)
            embed.set_image(url=self.itsfinegif)
            view = ui.View()
            embed.set_thumbnail(url=self.logoMsize)
            view.add_item(ui.Button(label='API Link', url=self.api_users, row=0))
            await interaction.response.send_message(f"<@{interaction.user.id}> Here:", embed=embed, view=view)
            
        else:
            print(userid)
            link = f'http://54.82.98.129/api/v1/users/{userid}/?format=json'
            headers = {'Authorization': []}
            headers['Authorization'] = token
            empty = ['\---------------']
            jsonify = requests.get(link, headers=headers).json()
            usr = jsonify["userdata"]
            urnm = jsonify["username"]
            embed = discord.Embed(color=0x7ac3e6)
            embed.add_field(name=f"**{urnm}'s userdata:**",value=usr, inline=False)
            view = ui.View()
            embed.set_thumbnail(url=self.logoSsize)
            view.add_item(ui.Button(label='API Link', url=self.api_users, row=0))
            await interaction.response.send_message(f"<@{interaction.user.id}> Here:", embed=embed, view=view)
            
    @app_commands.command(description='get your token')
    @app_commands.describe(username="Your username")
    @app_commands.describe(password="Your password")
    async def gettoken(self, interaction: Interaction, username: str, password: str) -> None:
        """get ur gettoken"""
        api = self.api_users
        status = requests.get(api, headers=self.headers)
        
        if status.status_code != 200:
            
            embed = discord.Embed(color=0xFF0000)
            embed.add_field(name=f"**Server Status:** [{status.status_code}]",value="**Oh no! Server is not responding!**", inline=False)
            embed.set_thumbnail(url=self.thumb)
            embed.set_image(url=self.errorgif)
            view = ui.View()
            view.add_item(ui.Button(label='API Link', url=self.api_users, row=0))
            await interaction.response.send_message(f"<@{interaction.user.id}> Here:", embed=embed, view=view) 

        elif len(get(api).json()) == 0:
            embed = discord.Embed(color=0xFFA500)
            embed.add_field(name=f"**Server Status** [{status.status_code}]:",value="**Your Database is empty!**", inline=False)
            embed.set_image(url=self.itsfinegif)
            view = ui.View()
            embed.set_thumbnail(url=self.logoMsize)
            view.add_item(ui.Button(label='API Link', url=self.api_users, row=0))
            await interaction.response.send_message(f"<@{interaction.user.id}> Here:", embed=embed, view=view)
            
        else:
            params = {'username': [], 'password': []}
            params['username'] = username
            params['password'] = password
            response = requests.post(self.api_token, json=params)
            data = response.json()
            embed = discord.Embed(color=0x7ac3e6)
            embed.add_field(name=f"**Your token:**",value=data, inline=False)
            view = ui.View()
            embed.set_thumbnail(url=self.logoSsize)
            view.add_item(ui.Button(label='API Link', url=self.api_users, row=0))
            await interaction.response.send_message(f"<@{interaction.user.id}> Here:", embed=embed, view=view)

    @app_commands.command(description='status')
    async def status(self, interaction: Interaction) -> None:
        """info about status"""
        status = get(self.api_status)
        if status.status_code != 200:

            embed = discord.Embed(color=0xFF0000)
            embed.add_field(name=f"**Server Status:** [{status.status_code}]",value="**Oh no! Server is not responding!**", inline=False)
            embed.set_thumbnail(url=self.thumb)
            embed.set_image(url=self.errorgif)
            view = ui.View()
            view.add_item(ui.Button(label='API Link', url=self.api_status, row=0))
            await interaction.response.send_message(f"<@{interaction.user.id}> Here:", embed=embed, view=view)
        else:
            ok = status.json().get('status')
            code = status.json().get('code')
            embed = discord.Embed(color=0x00FF00)
            embed.add_field(name=f"**Server Status:** [{ok}]",
            value=f"**Server is up and runing!**\n", inline=False)
            embed.set_thumbnail(url=self.thumb)
            embed.set_image(url=self.doggif)
            view = ui.View()
            view.add_item(ui.Button(label='API Link', url=self.api_status, row=0))
            embed.set_footer(text=f"Status Code: [{code}]")
            await interaction.response.send_message(f"<@{interaction.user.id}> Here:", embed=embed, view=view)

async def setup(bot: petville) -> None:
    await bot.add_cog(Admin(bot))
