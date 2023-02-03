import yt_dlp
import pathlib
import os
import pkg_resources

def main():
    __version__ = pkg_resources.get_distribution("youtubedlez")

    print(f"Easy Youtube Downloader {__version__}")
    print("(c) Stefano Pigozzi")
    print("Released under the GPL 3.0")
    print("-" * 80)
    print()

    dl_url = input("What video(s) do you want to download? ")

    while True:
        while True:
            dl_format = input("What format to you want the downloaded file(s) to have? ")
            video_formats = ['mp4', 'flv', 'webm', 'ogg', 'mkv', 'avi']
            audio_formats = ['best', 'aac', 'flac', 'mp3', 'm4a', 'opus', 'vorbis', 'wav']

            if dl_format in video_formats:
                postprocessors = [
                    {
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': dl_format,
                    },
                ]
                break
            elif dl_format in audio_formats:
                postprocessors = [
                    {
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': dl_format,
                    },
                ]
                break
            else:
                print("Invalid format specified")
                print("Formats available: ")
                print("Video: " + " ".join(video_formats))
                print("Audio: " + " ".join(audio_formats))


        dl_location = pathlib.Path.home().joinpath("Downloads")
        os.makedirs(name=dl_location, exist_ok=True)
        print(f"The downloads will be saved in: {dl_location}")

        print()
        with yt_dlp.YoutubeDL({
            "noplaylist": True,
            "prefer_ffmpeg": True,
            "outtmpl": f"{dl_location}/%(extractor)s__%(title)s.%(ext)s",
            "postprocessors": postprocessors,
            "addmetadata": True,
        }) as ytdl:
            ytdl.download([dl_url])
        print()

        print("Download complete!")
        print("-" * 80)


if __name__ == "__main__":
    main()