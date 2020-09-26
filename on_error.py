

# This file contains multiple on_error functions to be used in main.

async def printError(event, *args, **kwargs):
    errorMessage = args[0]
    print(errorMessage)
