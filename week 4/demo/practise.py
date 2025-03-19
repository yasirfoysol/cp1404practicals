"""
CP1404 Assignment 1 - Song List 1.0
Author: Yasir Foysol Rahib
Date: 2025-03-05
Description: A Python program to manage a song list with functionalities to display, add, mark as learned, and save songs.
GitHub Repository: [INSERT YOUR GITHUB LINK HERE]
"""

import os

# Constants
FILE_NAME = "songs.csv"
LEARNED = "l"
UNLEARNED = "u"


def load_songs():
    """Load songs from the CSV file into a list."""
    songs = []
    if not os.path.exists(FILE_NAME):
        print("No existing song file found, starting fresh.")
        return songs

    with open(FILE_NAME, "r") as file:
        for line in file:
            title, artist, year, status = line.strip().split(",")
            songs.append([title, artist, int(year), status])
    return songs


def display_songs(songs):
    """Display the list of songs sorted by year then title."""
    if not songs:
        print("No songs found. Add some first!")
        return

    songs.sort(key=lambda s: (s[2], s[0]))
    for i, song in enumerate(songs, 1):
        status = "*" if song[3] == UNLEARNED else " "
        print(f"{i}. {status} {song[0]:30} - {song[1]:20} ({song[2]})")

    learned_count = sum(1 for song in songs if song[3] == LEARNED)
    print(f"{learned_count} songs learned, {len(songs) - learned_count} songs still to learn.")


def add_song(songs):
    """Add a new song with proper input validation."""
    title = input("Enter song title: ").strip()
    while not title:
        print("Title cannot be blank!")
        title = input("Enter song title: ").strip()

    artist = input("Enter artist: ").strip()
    while not artist:
        print("Artist cannot be blank!")
        artist = input("Enter artist: ").strip()

    while True:
        try:
            year = int(input("Enter year: "))
            if year > 0:
                break
            else:
                print("Year must be greater than 0.")
        except ValueError:
            print("Invalid input; enter a valid number.")

    songs.append([title, artist, year, UNLEARNED])
    print(f"{title} by {artist} ({year}) added to song list.")


def mark_learned(songs):
    """Mark an unlearned song as learned."""
    unlearned_songs = [song for song in songs if song[3] == UNLEARNED]
    if not unlearned_songs:
        print("No more songs to learn!")
        return

    while True:
        try:
            song_number = int(input("Enter the number of a song to mark as learned: ")) - 1
            if 0 <= song_number < len(songs) and songs[song_number][3] == UNLEARNED:
                songs[song_number][3] = LEARNED
                print(f"{songs[song_number][0]} by {songs[song_number][1]} learned!")
                break
            elif songs[song_number][3] == LEARNED:
                print(f"You have already learned {songs[song_number][0]}")
            else:
                print("Invalid song number.")
        except (ValueError, IndexError):
            print("Invalid input; enter a valid number.")


def save_songs(songs):
    """Save all songs to the CSV file."""
    with open(FILE_NAME, "w") as file:
        for song in songs:
            file.write(",".join(map(str, song)) + "\n")
    print(f"{len(songs)} songs saved to {FILE_NAME}")


def main():
    """Main menu loop for the program."""
    print("Song List 1.0 - by Yasir Foysol Rahib")
    songs = load_songs()

    while True:
        print("\nMenu:\nD - Display songs\nA - Add new song\nC - Complete a song\nQ - Quit")
        choice = input(">>> ").strip().upper()

        if choice == "D":
            display_songs(songs)
        elif choice == "A":
            add_song(songs)
        elif choice == "C":
            mark_learned(songs)
        elif choice == "Q":
            save_songs(songs)
            print("Make some music!")
            break
        else:
            print("Invalid menu choice")


if __name__ == "__main__":
    main()
