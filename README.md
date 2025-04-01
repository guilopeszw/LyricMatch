*About*

=AI transcriber to get lyrics from any song (works better in english songs) using AssemblyAI's free API, that requires the user to input an .mp3 or .wav file. To make things easier, using yt-dlp, you only have to input a youtube link to the song of your choice and the library will download it into an mp3 file, which will be automatically transcribed and saved in a .txt (bonus: all files are saved locally, which means they're accessable at any moment after using LyricMatch)





## Requisites

- Python: https://www.python.org/downloads/
- YoutubeToWav: https://github.com/jschuhmann47/youtubeToWav 
- yt-dlp: https://github.com/yt-dlp/yt-dlp
- ffmpeg: https://ffmpeg.org/download.html
- AssemblyAI: https://www.assemblyai.com/app

(I'd advise you to, in order to understand the program, first read jschuhmann47's GitHub post, it'll help configure the project and make sure you download and set up everything correctly).
## Environment Variables

In order to run this project, you'll need the following variables in your environment .env:


`ffmpeg`

`yt-dlp`

(Make sure you correctly download ffmpeg executables according to your OS, and not the source-code)


all credits to jschumann47! this was made fully for educational purposes and couldn't have been done without him!
