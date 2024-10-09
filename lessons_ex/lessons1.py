"""
Создай класс Album у которого есть поля

- Исполнитель (artist) - строка
- Название (title) - строка
- Треки (tracks) - это **список**

**Создай два экземпляра album_1 и album_2**

Исполнитель: Queen

Название: Killer Queen

Треки: Brighton rock, Killer Queen, Tenement Funster

Исполнитель: Metallica

Название: Black Album

Треки: Enter Sandman, Sad But True, Holier Than Thou
"""


class MusicAlbum:
    artist: str
    title: str
    tracks: list

    def __init__(self, artist, title, tracks):
        self.artist = artist
        self.title = title
        self.tracks = tracks


album_1 = MusicAlbum('Queen','Killer Queen','Brighton rock, Killer Queen, Tenement Funster')

album_2 = MusicAlbum('Metallica','Black Album', 'Enter Sandman, Sad But True, Holier Than Thou')


# код для проверки
print(album_1.artist, album_1.title, len(album_1.tracks), "треков")  # Queen Killer Queen 3 треков
print(album_2.artist, album_2.title, len(album_2.tracks), "треков")  # Metallica Black Album 3 треков

"""
Создай класс Student (студент) с полями

- Имя (name) - строка
- Курс (course) - целое число

Создай два экземпляра

- Алиса , 3 [курс]
- Маргарита , 2 [курс]
"""


class Student:
    name: str
    course: int
    def __init__(self,name,course):
        self.name = name
        self.course = course



student_1 = Student('Алина', 3)
student_2 = Student('Маргарита', 2)


# код для проверки
print(student_1.name, student_1.course)  # Алиса 3
print(student_2.name, student_2.course)  # Маргарита 2