#from urllib.parse import urlencode, quote_plus
#from urllib import parse
import requests, urllib.parse


#get user input
badge = input("Name of badge: ")
color_input = input("Color with the #: ")

#Post processing to encode and remove spaces
a = urllib.parse.quote(color_input)
underscores = badge.replace(" ", "_")
nospaces = badge.replace(" ", "")

url = f'(https://img.shields.io/badge/{underscores}-{a}?style=for-the-badge&logo={nospaces}&logoColor=white)'
front = ("| " + badge + " | ")
mdrender = ("!" + "[" + badge + "]")
codesnippet = ("`" + url + "`")
md = ("`" + mdrender + url + "`")
#Deliver the result to terminal
#print(front + mdrender + url + "|" + codesnippet)
print(front + mdrender + url + "|" + md + "|" )
