import xml.etree.ElementTree as ET

tree = ET.parse('ArtisteDevoir.xml')
root = tree.getroot()

def search_artist(name):
    for artist in root.findall('.//artiste'):
        if artist.attrib['nom'].lower() == name.lower():
            return artist
    return None

def display_artist(artist):
    print(f"Name: {artist.attrib['nom']}")
    print(f"City: {artist.attrib['ville']}")
    print(f"Biography: {artist.find('biographie').text}")
    website = artist.find('site')
    if website is not None:
        print(f"Website: {website.attrib['url']}")
    print()

def display_albums(artist):
    artist_ref = artist.attrib['no']
    for album in root.findall(".//album"):
        ref_artiste = album.find('ref-artiste').attrib['ref']
        if ref_artiste == artist_ref:
            print(f"Album Title: {album.find('titre').text}")
            print(f"Release Year: {album.attrib['annee']}")
            print("Songs:")
            for song in album.findall('chansons/chanson'):
                print(f" - {song.text}")
            print()


while True:
    print("Welcome to the Music Database!")
    print("1. Search for an artist")
    print("2. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter the artist's name: ")
        artist = search_artist(name)
        if artist is None:
            print("Artist not found.")
        else:
            display_artist(artist)
            display_albums(artist)
    elif choice == '2':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")