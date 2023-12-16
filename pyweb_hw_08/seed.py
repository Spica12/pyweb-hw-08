from models import Author, Quote
from mongoengine import NotUniqueError
import json

if __name__ == "__main__":
    with open("authors.json") as file:
        data = json.load(file)
        for el in data:
            try:
                author = Author(
                    fullname=el.get("fullname"),
                    born_date=el.get("born_date"),
                    born_location=el.get("born_location"),
                    description=el.get("description"),
                )
                author.save()
            except NotUniqueError:
                print(f"Author {el.get('fullname')} exists.")

    # with open("qoutes.json", "r", encoding="utf-8") as file:
    with open("qoutes.json") as file:
        data = json.load(file)
        for el in data:
            author, *_ = Author.objects(fullname=el.get("author"))
            qoute = Quote(
                quote=el.get("quote"),
                tags=el.get("tags"),
                author=author,
            )

            qoute.save()
