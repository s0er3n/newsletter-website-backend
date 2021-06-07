from sys import argv
import uvicorn
from os import environ as env


def argparser():
    """ Parses CLI arguments into dictionary form
        FLAGS {'flag': True}
            --flag, -flag

        KEY/VALUE {'key': 'value'}
            key=value
    """
    args = argv[1:]
    i = 0
    parsed_args = {}

    while i < len(args):
        arg = args[i]

        if "=" in arg:
            keyvalue = arg.split("=")
            parsed_args[keyvalue[0]] = keyvalue[1]
        elif arg.startswith("--") and len(arg) > 1:
            parsed_args[arg[2:]] = True
        elif arg.startswith("-") and len(arg) > 1:
            parsed_args[arg[1:]] = True
        else:
            print(
                f"Invalid Argument '{arg}' (flags: '-arg', other: 'key=value'")

        i += 1
    return parsed_args


def printhelp():
    print(
        "USAGE: 'newsletter [host=0.0.0.0] [port=80] [--reload]' [optional argument]")


def main():
    args = argparser()
    host = args.get("host", "localhost")
    port = args.get("port", 8000)
    reload = args.get("reload", args.get("r", False))

    # Get other variables
    other_keys = [
        key for key in list(args.keys())
        if key not in ["host", "port", "reload"]
    ]

    # Set Environment Variables
    for key in other_keys:
        value = args[key]

        if isinstance(value, bool):
            value = str(1 if value else 0)

        env[key] = value

    uvicorn.run("newsletter_api.app:app", host=host, port=port, reload=reload)
