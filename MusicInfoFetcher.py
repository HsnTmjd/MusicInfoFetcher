import requests
import json
from datetime import datetime

while True:
    print("This is a program that will display the names of a given number of songs by the specified artist.")
    x = input("To proceed type 'yes' and 'no' if you don't want to: ").lower().strip()

    if x == "yes":
        artist_name = input("Enter the artist name: ")
        num_songs = int(input("Enter the number of songs for which you want to know the names: "))
        response = requests.get(f"https://itunes.apple.com/search?entity=song&limit={num_songs}&term={artist_name}")

        o = response.json()

        print(f"Here is a list of {num_songs} songs of {artist_name}_")
        for i, result in enumerate(o["results"], start=1):
            print(f"{i}. {result['trackName']}")

            link = result["trackViewUrl"]
            print(f"   Click here to visit the song: {link}")


            release_date = datetime.fromisoformat(result['releaseDate'].replace('Z', '+00:00'))
            formatted_date = release_date.strftime('%dth %B, %Y')
            print(f"   Release Date: {formatted_date}")

        break
    elif x == "no":
        print("Thank you")
        break
    else:
        print("Invalid input.")
