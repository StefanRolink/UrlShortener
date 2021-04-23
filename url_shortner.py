#!/usr/bin/env python3
"""
Small tinyurl cmd line tool to shorten urls.

Created 23-04-2021. Stefan
"""

import argparse
import pyshorteners
import pyperclip

from urllib3.exceptions import ReadTimeoutError


def init_argparser() -> argparse.ArgumentParser:
    """Argument configuration."""
    shorteners_list = pyshorteners.Shortener().available_shorteners

    parser = argparse.ArgumentParser(description='Small tiny url tool to shorten url')
    parser.add_argument('shortner', choices=shorteners_list, default='tinyurl', nargs='?', help='The chosen url shortner.')
    parser.add_argument('-u', '--url', dest='url', type=str, required=True, help='The URL to shorten.')
    return parser


def shorten(url: str, shortner: str = 'tinyurl') -> str:
    """Shorts an url, returns url-string."""
    short_url: str

    shortener = pyshorteners.Shortener()
    if shortner == 'tinyurl':
        short_url = shortener.tinyurl.short(url)
    elif shortner == 'chilpit':
        short_url = shortener.chilpit.short(url)
    elif shortner == 'clckru':
        short_url = shortener.clckru.short(url)
    elif shortner == 'dagd':
        short_url = shortener.dagd.short(url)
    elif shortner == 'gitio':
        short_url = shortener.gitio.short(url)
    elif shortner == 'isgd':
        short_url = shortener.isgd.short(url)
    elif shortner == 'nullpointer':
        short_url = shortener.nullpointer.short(url)
    elif shortner == 'osdb':
        short_url = shortener.osdb.short(url)
    elif shortner == 'owly':
        short_url = shortener.owly.short(url)
    elif shortner == 'qpsru':
        short_url = shortener.qpsru.short(url)
    elif shortner == 'nullpointer':
        short_url = shortener.nullpointer.short(url)

    return short_url


def copy_to_clipboard(string: str) -> None:
    """Copy string to system's clipboard."""
    pyperclip.copy(string)


def main() -> None:
    """Shorten url, copy to clipboard and print to stdout."""
    parser = init_argparser()
    args = parser.parse_args()

    try:
        short_url = shorten(args.url, args.shortner)
    except ReadTimeoutError:
        print(f'Warning: {args.url} does not seem to exsist.')

    copy_to_clipboard(short_url)
    print(short_url)


if __name__ == '__main__':
    main()
