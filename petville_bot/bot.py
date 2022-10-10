from __future__ import annotations

import asyncio
import os
import sys
import traceback

import aiohttp
import discord
from discord.ext import commands
from discord.ext.commands import ExtensionFailed, ExtensionNotFound, NoEntryPointError
from dotenv import load_dotenv
from utils import locale_v2


load_dotenv()

initial_extensions = ['cogs.admin', 'cogs.errors']

# intents required
intents = discord.Intents.default()
intents.message_content = True

BOT_PREFIX = '-'

# todo claer white space


class petville(commands.Bot):
    debug: bool
    bot_app_info: discord.AppInfo

    def __init__(self) -> None:
        super().__init__(command_prefix=BOT_PREFIX, case_insensitive=True, intents=intents)
        self.session: aiohttp.ClientSession = None
        self.bot_version = 'Alpha'
        self.tree.interaction_check = self.interaction_check

    @staticmethod
    async def interaction_check(interaction: discord.Interaction) -> bool:
        locale_v2.set_interaction_locale(interaction.locale)
        return True

    @property
    def owner(self) -> discord.User:
        return self.bot_app_info.owner

    async def on_ready(self) -> None:
        await self.tree.sync()
        print(f"\nLogged in as: {self.user}\n\nPetVille is Ready!")
        print(f"Version: {self.bot_version}")

        # bot presence
        activity_type = discord.ActivityType.playing
        await self.change_presence(activity=discord.Activity(type=activity_type, name="with pets!"))

    async def setup_hook(self) -> None:
        if self.session is None:
            self.session = aiohttp.ClientSession()

        try:
            self.owner_id = int(os.getenv('OWNER_ID'))
        except ValueError:
            self.bot_app_info = await self.application_info()
            self.owner_id = self.bot_app_info.owner.id

        self.setup_cache()
        await self.load_cogs()
        # await self.tree.sync()

    async def load_cogs(self) -> None:
        for ext in initial_extensions:
            try:
                await self.load_extension(ext)
            except (
                ExtensionNotFound,
                NoEntryPointError,
                ExtensionFailed,
            ):
                print(f'Failed to load extension {ext}.', file=sys.stderr)
                traceback.print_exc()

    @staticmethod
    def setup_cache() -> None:
        try:
            open('data/cache.json')
        except FileNotFoundError:
            get_cache()

    async def close(self) -> None:
        await self.session.close()
        await super().close()

    async def start(self, debug: bool = False) -> None:
        self.debug = debug
        return await super().start(os.getenv('TOKEN'), reconnect=True)


def run_bot() -> None:
    bot = petville()
    asyncio.run(bot.start())


if __name__ == '__main__':
    run_bot()
