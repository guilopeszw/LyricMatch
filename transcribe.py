import requests
import assemblyai as aai

from youtubeToWav.youtubetowav import download_from_url

# insert here your AssemblyAI API Key
aai.settings.api_key = "60d926e3030342abb2c1d08976231ec8"
transcriber = aai.Transcriber()

print("")
print("Lyrics: ")
transcript = transcriber.transcribe('output.wav')

# I wanted to be able to have the transcription as a .txt file, so I used the 'open' method
transcription = open("text_output.txt", 'w')
print(transcript.text, file=transcription)
transcription.close()
