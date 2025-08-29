from src.utils.logo import return_logo
import os

from src.install_song_from_url import install_from_url


def create_directory_for_downloads():
    try:
        os.mkdir(os.path.join(os.path.expanduser('~'), "Music", "smi"))
    except FileExistsError:
        pass


if __name__ == '__main__':
    create_directory_for_downloads()

    print(return_logo() + " spotify-music-installer")
    print("By Vortique")

    while (True):
        print("\nWhat do you want to do?:")
        print("1. Install Song From URL")
        print("2. Install Songs From Playlist (URL)")
        print("3. Install Songs From Artist (URL)")
        print("4. Set ClientID and ClientSecret")
        print("5. Exit")

        if (input("> ") == "1"):
            url: str = input("Enter URL of song (You can get it from right-click+share): ")

            install_from_url(url)
        