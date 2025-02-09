*About*

I had the idea of using an AI transcriber to get lyrics from any song (in this case, works best if in english). I found an API (AssemblyAI) that requires the user to input an .mp4 or .wav file, so that gave me the idea to try and link the transcriber with an audio downloader (which in this case, was yt-dlp/youtubetowav). 

The idea is that the user will input an YouTube link and get a .wav file from it, which will be automatically be transcribed and turned into a .txt file.






## Requisites

- Python: https://www.python.org/downloads/
- YoutubeToWav: https://github.com/jschuhmann47/youtubeToWav 
- yt-dlp: https://github.com/yt-dlp/yt-dlp
- ffmpeg: https://ffmpeg.org/download.html
- AssemblyAI: https://www.assemblyai.com/app

(I'd recommend you to first read jschuhmann47's GitHub post, it'll help you configure the project and make sure you download everything correctly).
## Environment Variables

In order to run this project, you'll need the following variables in your environment .env:


`ffmpeg`

`yt-dlp`

(Make sure you correctly download ffmpeg executables according to your OS, and not the source-code)


# all credits to jschumann47! this was made fully for educational purposes and couldn't have been done without him!# all credits to jschumann47! this was made fully for educational purposes and couldn't have been done without him!
