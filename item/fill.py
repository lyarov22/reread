from .models import Publisher

publishers = [
    "Эксмо",
    "АСТ",
    "Бомбора",
    "Миф",
    "Росмэн",
    "Азбука",
]

for name in publishers:
    Publisher.objects.create(name=name)
