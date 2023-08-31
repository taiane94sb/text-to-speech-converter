from gtts import gTTS
import os

text = open('demo.txt', 'r').read()
output = gTTS(text=text, lang='en', slow=False)
output.save('fileoutput.mp3')
os.system("start fileoutput.mp3")

text2 = open('demo2.txt', 'r').read()
output = gTTS(text=text2, lang='pt-BR', slow=False)
output.save('fileoutput2.mp3')
os.system("start fileoutput2.mp3")
