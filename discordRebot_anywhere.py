"""
To make non strict mode Roles and Permissions checks for discord-rebot

Example::

   Fn.auth = Roles['Admin'] # this will not allow DM or from other guild
   
   Fn.auth = Anywhere(Roles['Admin']) # will allow
   
"""

import asyncio
import discord
from discordRebot import Converter, Authorize


class Anywhere:
    """
    To allow message from anywhere, for authorizing Roles or Permissions
    """

    bot = NotImplemented

    def __init__(self, auths, bot=None):
        """
        Args:
            auth (Roles, Permissions, Set(Union[Roles, Permissions])): authorized
        """

        self.auths = auths
        if bot is not None:
            self.bot = bot

    def __call__(self, message):
        """An auth (since self is Callable[[Message], bool] in discordRebot.manager.Auth)
        
        Args:
            message (Message): message passed to callback
        
        Returns:
            (bool): True if authorized else False
        """

        if self.bot is NotImplemented:
            raise NotImplementedError("set Anywhere.bot or pass bot")
        Convert = Converter(self.bot)

        member = asyncio.run(Convert(message, str(message.author.id), discord.Member))
        message = type("dummy message", (), {})
        message.author = member

        return bool(Authorize(self.auths, message))
