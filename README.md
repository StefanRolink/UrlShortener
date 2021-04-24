# UrlShortener
Simple command-line URL shortner

# Installation
Install with: 
`ln -s $(pwd)/url_shortner.py /usr/local/bin/us`

# Usage
usage: us [-h] [-s <shortener>] url

positional arguments:
  url                   The URL to shorten.

optional arguments:
  -h, --help            Show this help message and exit
  -s, --shortener       The chosen url shortener.
                        Choose from: [adfly,bitly,chilpit,clckru,cuttly,dagd,gitio,isgd,nullpointer,osdb,owly,post,qpsru,shortcm,tinycc or tinyurl]
