
# Import the required module for text
# to speech conversion
from gtts import gTTS

import PyPDF2

with open("simple.pdf", "rb") as files:
    pdfReader = PyPDF2.PdfFileReader(files)
    count = pdfReader.numPages
    output = []
    for i in range(count):
        page = pdfReader.getPage(i)
        output.append(page.extractText())
    print(output)

# This module is imported so that we can
# play the converted audio
import os
text = ""
for items in output:
    text += items
# The text that you want to convert to audio
mytext = text
print(mytext)
# Language in which you want to convert
language = 'ru'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome_russian.mp3")