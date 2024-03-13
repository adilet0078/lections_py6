# class User:
#     def __init__(self, username, age, email, subscription=False, password=None):
#         self.__username = username
#         self.__age = age
#         self.__email = email
#         self.__subscription = subscription
#         self.__password = password
#         self.__playlist = []

#     def validate_email(self):
#         if "@" not in self.__email:
#             raise ValueError("Invalid email format")

#     def validate_password(self):
#         # Your password validation logic
#         pass

#     def validate_age(self):
#         # Your age validation logic
#         pass

#     def subscribe(self):
#         self.__subscription = True
#         print(f"User {self.__username} has subscribed.")

#     def add_to_playlist(self, song):
#         self.__playlist.append(song)
#         print(f"Added {song} to the playlist of user {self.__username}.")

#     def listen_to_song(self, song):
#         if self.__subscription:
#             print(f"User {self.__username} is playing {song}.")
#         else:
#             print("Please subscribe to listen to songs")

#     def listen_to_playlist(self):
#         print(f"User {self.__username} is listening to their playlist:")
#         for song in self.__playlist:
#             self.listen_to_song(song)


# class Genre:
#     def __init__(self, name):
#         self.name = name


# class Music:
#     def __init__(self, title, author, genre, duration):
#         self.title = title
#         self.author = author
#         self.genre = genre
#         self.duration = duration


# class Employee(User):
#     def __init__(self, username, age, email, subscription=False, password=None, role=None, platform=None):
#         super().__init__(username, age, email, subscription, password)
#         self.role = role
#         self.platform = platform


# class Platform:
#     def __init__(self, name):
#         self.name = name
#         self.songs = []
#         self.genres = []
#         self.subscribed_users = []
#         self.unsubscribed_users = []

#     def view_all_songs(self):
#         print("All songs on the platform:")
#         for song in self.songs:
#             print(song.title)

#     def view_songs_by_genre(self, genre_name):
#         print(f"All songs in the genre {genre_name}:")
#         for song in self.songs:
#             if song.genre.name == genre_name:
#                 print(song.title)

#     def subscribe_user(self, user):
#         user.subscribe()
#         self.subscribed_users.append(user)
#         print(f"User {user._User__username} subscribed to {self.name}.")

#     def search_song_by_title(self, title):
#         print(f"Searching for the song with title '{title}':")
#         for song in self.songs:
#             if song.title == title:
#                 print(f"Found: {song.title} by {song.author} ({song.genre.name})")
#                 return song
#         print("Song not found.")
#         return None

#     def add_song_to_user_playlist(self, user, song):
#         user.add_to_playlist(song)

#     def remove_song(self, admin, song):
#         if admin.role == "admin":
#             self.songs.remove(song)
#             print(f"Song {song.title} removed from the platform by admin.")

#     def add_genre(self, admin, genre):
#         if admin.role == "admin":
#             self.genres.append(genre)
#             print(f"Genre {genre.name} added to the platform by admin.")

#     def remove_genre(self, admin, genre):
#         if admin.role == "admin":
#             self.genres.remove(genre)
#             print(f"Genre {genre.name} removed from the platform by admin.")

#     def block_user(self, admin, user):
#         if admin.role == "admin":
#             self.unsubscribed_users.append(user)
#             if user in self.subscribed_users:
#                 self.subscribed_users.remove(user)
#             print(f"User {user._User__username} blocked by admin.")

#     def delete_user(self, admin, user):
#         if admin.role == "admin":
#             if user in self.subscribed_users:
#                 self.subscribed_users.remove(user)
#             if user in self.unsubscribed_users:
#                 self.unsubscribed_users.remove(user)
#             print(f"User {user._User__username} deleted by admin.")


# # Пример использования:
# user1 = User("user1", 25, "user1@example.com")
# genre1 = Genre("Rock")
# song1 = Music("Song 1", "Artist 1", genre1, "4:30")
# platform1 = Platform("Spotify")

# # Добавление песни на платформу
# platform1.songs.append(song1)
# platform1.view_all_songs()

# # Добавление пользователя на платформу
# platform1.subscribe_user(user1)

# # Просмотр всех песен на платформе
# platform1.view_all_songs()

# # Просмотр песен определенного жанра
# platform1.view_songs_by_genre("Rock")

# # Поиск песни по названию
# found_song = platform1.search_song_by_title("Song 1")

# # Добавление песни в плейлист пользователя
# platform1.add_song_to_user_playlist(user1, found_song)

# # Удаление песни с платформы (требуется админские права)
# admin = Employee("admin", 30, "admin@example.com", role="admin", platform=platform1)
# platform1.remove_song(admin, found_song)

# # Блокировка пользователя (требуется админские права)
# platform1.block_user(admin, user1)

# # Удаление пользователя (требуется админские права)
# platform1.delete_user(admin, user1)
