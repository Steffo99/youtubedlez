import yt_dlp
import pathlib
import os

video_formats = ['mp4', 'flv', 'webm', 'ogg', 'mkv', 'avi']
audio_formats = ['best', 'aac', 'flac', 'mp3', 'm4a', 'opus', 'vorbis', 'wav']

def main():
    print(f"Easy Youtube Downloader")
    print("(c) Stefano Pigozzi")
    print("Licensed under the EUPL-1.2")
    print("-" * 80)
    print()

    dl_location = pathlib.Path.home().joinpath("Downloads")
    os.makedirs(name=dl_location, exist_ok=True)
    print(f"Downloads will be saved in: {dl_location}")
    print("-" * 80)
    print()

    arguments = {
        "noplaylist": True,
        "prefer_ffmpeg": True,
        "restrictfilenames": True,
        "windowsfilenames": True,
    }
    while True:
        dl_format = input("What format to you want the downloaded file(s) to have? ")

        if dl_format in video_formats:
            arguments |= {
                "format": "best",
                "postprocessors": [
                    {
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': dl_format,
                    },
                ],
            }
            break
        elif dl_format in audio_formats:
            arguments |= {
                "format": "bestaudio/best",
                "postprocessors": [
                    {
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': dl_format,
                    },
                    {
                        'key': 'FFmpegMetadata',
                        'add_metadata': True,
                        'add_chapters': False,
                        'add_infojson': False,
                    },
                ],
            }
            break
        else:
            print("Invalid format specified")
            print("Formats available: ")
            print("Video: " + " ".join(video_formats))
            print("Audio: " + " ".join(audio_formats))
            print()
            continue
    print("-" * 80)
    print()

    while True:
        try:
            dl_url = input("What video(s) do you want to download? ")
            with yt_dlp.YoutubeDL({
                "outtmpl": f"{dl_location}/%(extractor)s__%(title)s.%(ext)s",
                **arguments,
                "postprocessors": [*arguments.get("postprocessors", [])],
            }) as ytdl:
                ytdl.download([dl_url])
        except KeyboardInterrupt:
            print("Exiting...")
            break
        except Exception:
            print("Download error.")
        else:
            print("Download complete!")
        finally:
            print("-" * 80)
            print()


if __name__ == "__main__":
    main()
