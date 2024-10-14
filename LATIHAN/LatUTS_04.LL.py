class SongNode:
    def __init__(self, title, artist, song):
        self.title = title
        self.artist = artist
        self.song = song
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None 
        self.current = None

    def add_song(self, title, artist, song):
        new_song = SongNode(title, artist, song)
        if self.head is None:
            self.head = new_song
            self.current = new_song
            new_song.next = new_song
            new_song.prev = new_song
        else:
            tail = self.head.prev
            tail.next = new_song
            new_song.prev = tail
            new_song.next = self.head
            self.head.prev = new_song

    def play_current_song(self):
        if self.current is None:
            print("Playlist kosong.")
        else:
            print(f"Now Playing: {self.current.title} by {self.current.artist}")

    def next_song(self):
        if self.current is None:
            print("Playlist kosong.")
        else:
            self.current = self.current.next
            self.play_current_song()

    def prev_song(self):
        if self.current is None:
            print("Playlist kosong.")
        else:
            self.current = self.current.prev
            self.play_current_song()

    def show_playlist(self):
        if self.head is None:
            print("Playlist kosong.")
            return

        print("Playlist:")
        song = self.head
        while True:
            print(f"{song.title} by {song.artist}")
            song = song.next
            if song == self.head:
                break

def menu():
    print("\n=== Playlist Menu ===")
    print("1. Add Song")
    print("2. Play Current Song")
    print("3. Next Song")
    print("4. Previous Song")
    print("5. Show Playlist")
    print("6. Exit")

playlist = Playlist()

while True:
    menu()
    choice = input("Pilih opsi (1-6): ")

    if choice == '1':
        title = input("Masukkan judul lagu: ")
        artist = input("Masukkan nama penyanyi: ")
        song = input("Masukkan lirik lagu (opsional): ")
        playlist.add_song(title, artist, song)
        print(f"Lagu '{title}' oleh {artist} berhasil ditambahkan.")

    elif choice == '2':
        playlist.play_current_song()

    elif choice == '3':
        playlist.next_song()

    elif choice == '4':
        playlist.prev_song()

    elif choice == '5':
        playlist.show_playlist()

    elif choice == '6':
        print("Keluar dari program. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")