from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=255)

    MALE = "M"
    FEMALE = "F"
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, "Женщина")
    ]
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Book(models.Model):
    name = models.CharField(max_length=120)
    year_of_public = models.DateField()

    BOEVIK = "BO"
    FANTASTIKA = "FA"
    DETECTIV = "DE"
    LOVEROMAN = "LR"
    PRICLUCHENIYA = "PR"
    TRILLER = "TR"
    HISTORICALROMAN = "HR"
    MISTIKA = "MI"
    DRAMA = "DR"
    UGASI = "UG"
    SKAZKA = "SK"
    NONAME = "NN"
    GENRES = [
        (BOEVIK, "Боевик"),
        (FANTASTIKA, "Фантастика"),
        (DETECTIV, "Детектив"),
        (LOVEROMAN, "Любовный роман"),
        (PRICLUCHENIYA, "Приключения"),
        (TRILLER, "Триллер"),
        (HISTORICALROMAN, "Исторический роман"),
        (MISTIKA, "Мистика"),
        (DRAMA, "Драма"),
        (UGASI, "Ужасы"),
        (SKAZKA, "Сказка"),
        (NONAME, "--")
    ]
    genres = models.CharField(max_length=2, choices=GENRES, default=NONAME)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

