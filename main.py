from bs4 import BeautifulSoup
from gtts import gTTS
import requests
import html


url="https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

# Make a GET request to fetch the raw HTML content
f = open("test.html", "r")
language = 'en'
# print(f.read())
# Parse the html content
soup = BeautifulSoup(f, "lxml")
for element in soup.find_all("li"):
    print(element.text) # print the parsed data of html
    myobj = gTTS(text=element.text, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save(element.text+".mp3")

    # Playing the converted file
