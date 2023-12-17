import sys
import os

sys.path.append(os.path.join(os.getcwd(), "src"))

from src.seed import delete_collections, seed_authors_from_json, seed_qoutes_from_json
from src.models import Author, Quote


def test_seed_authors_from_json():
    seed_authors_from_json()

    authors = Author.objects()
    assert authors[0].fullname == "Albert Einstein"
    assert authors[1].fullname == "Steve Martin"


def test_seed_qoutes_from_json():
    seed_authors_from_json()
    seed_qoutes_from_json()

    quotes = Quote.objects()

    assert (
        quotes[0].quote
        == "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”"
    )

    assert (
        quotes[1].quote
        == "“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”"
    )

    assert (
        quotes[2].quote
        == "“Try not to become a man of success. Rather become a man of value.”"
    )

    assert (
        quotes[3].quote
        == "“A day without sunshine is like, you know, night.”"
    )


def test_delete_collections_authors():
    model = Author
    delete_collections(model)
    collection = model.objects()
    print("Result: ", collection, type(collection))
    assert str(collection) == "[]"
