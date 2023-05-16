import os

from pytube import YouTube, exceptions

print('-' * 40)
print(f'{"YouTube Downloader":^38}')
print('-' * 40)

while True:
    url = input("Enter here the URL: ").strip()
    try:
        yt_link = YouTube(url)

    except exceptions.RegexMatchError:
        print("This isn't a valid URL, try again.")
        continue

    video_or_audio = input(
        "You want to download video or audio? ").lower().strip()

    destination = input('''Enter the destination to save the download:
>>> ''')
    destination = r'{}'.format(destination)

    if video_or_audio == 'video':
        try:
            print('Downloading...')

            download_video = yt_link.streams.get_highest_resolution()
            download_video.download(output_path=destination)

            print(f'"{yt_link.title}" downloaded successfully!')

        except Exception:
            print('Sorry, for some reason we can\'t download this video.')

    elif video_or_audio == 'audio':
        try:
            print('Downloading...')

            download_audio = yt_link.streams.filter(only_audio=True).first()
            out_file = download_audio.download(output_path=destination)

            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

            print(f'"{yt_link.title}" downloaded successfully!')

        except Exception:
            print('Sorry, for some reason we can\'t download this audio.')

    else:
        while video_or_audio != 'video' and video_or_audio != 'audio':
            print("This isn't a valid option, try again.")
            video_or_audio = input(
                "You want to download video or audio? ").lower().strip()
