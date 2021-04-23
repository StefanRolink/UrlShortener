#!/usr/bin/env python3
"""
Small tinyurl cmd line tool to shorten urls.

Created 23-04-2021. Stefan
"""

import argparse
import pyshorteners
import pyperclip

parser: argparse.ArgumentParser


def init_argparser() -> None:
    """Argument configuration."""
    global parser
    parser = argparse.ArgumentParser(description='Small tiny url tool to shorten url')
    #  parser.add_argument('-s', '--shortner', dest=shortner, required=False, default=TinyUrl, help='The chosen url shortner')
    parser.add_argument('-u', '--url', dest='url', type=str, required=True, help='The URL to shorten.')
    # TODO: list command: to show available shortners.


def shorten(url: str) -> str:
    """Shorts an url, returns url-string."""
    shortener = pyshorteners.Shortener()
    return shortener.tinyurl.short(url)


def copy_to_clipboard(string: str) -> None:
    """Copy string to system's clipboard."""
    pyperclip.copy(string)


def main() -> None:
    """Shorten url, copy to clipboard and print to stdout."""
    global parser

    init_argparser()
    args = parser.parse_args()

    short_url = shorten(args.url)
    copy_to_clipboard(short_url)
    print(short_url)


if __name__ == '__main__':
    main()
