from discord import app_commands


class NotOwner(app_commands.AppCommandError):
    """Raised when a command is used by a user who is not the owner of the bot."""

    pass


class BadArgument(app_commands.AppCommandError):
    """Raised when a command's argument could not be found."""

    pass


class ResponseError(app_commands.AppCommandError):
    """
    Raised whenever an empty response is given by the Riot server.
    """

    pass


class HandshakeError(app_commands.AppCommandError):
    """
    Raised whenever there's a problem while attempting to communicate with the local Riot server.
    """

    pass


class AuthenticationError(app_commands.AppCommandError):
    """
    Raised whenever there's a problem while attempting to authenticate with the Riot server.
    """

    pass


class DatabaseError(app_commands.AppCommandError):
    """
    Raised whenever there's a problem while attempting to access the database.
    """

    pass
