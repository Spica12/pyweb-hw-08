from mongoengine import (
    Document,
    connect,
    StringField,
    ReferenceField,
    ListField,
    CASCADE,
)
import configparser
import pathlib

file_config = (
    pathlib.Path(__file__).parent.parent.joinpath("configs").joinpath("config.ini")
)
config = configparser.ConfigParser()
config.read(file_config)

user = config.get("DEV_MONGO_DB", option="USER")
password = config.get("DEV_MONGO_DB", option="PASSWORD")
db = config.get("DEV_MONGO_DB", option="DB_NAME")

uri = f"mongodb+srv://{user}:{password}@cluster0.ae7t2cd.mongodb.net/?retryWrites=true&w=majority"
print(uri)

connect(db=db, host=uri)
print('Connected')

class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=120)
    description = StringField()

    meta = {"collection": "authors"}


class Quote(Document):
    tags = ListField(StringField(max_length=15))
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField()

    meta = {"collection": "qoutes"}
