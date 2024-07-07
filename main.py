from pytube import YouTube
import os


def download_audio(url, output_path):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_path)
        print("Audio download complete!")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":

    youtube_links = [
        'https://www.youtube.com/watch?v=SuuypjzzqRw',

    ]

    download_option = input("Download video (v) or audio (a)? ")

    desktop_path = os.path.expanduser("~/Desktop")
    audio_path = os.path.join(desktop_path, "audio.mp3")

    for youtube_link in youtube_links:

        if download_option.lower() == "v":
            yt = YouTube(youtube_link)
            stream = yt.streams.get_highest_resolution()
            stream.download(desktop_path)
            print(f"Video download complete. Downloaded {youtube_link}")

        elif download_option.lower() == "a":
            download_audio(youtube_link, desktop_path)
            print(f"Audio download complete. Downloaded {youtube_link}")

        else:
            print("Invalid option.")
