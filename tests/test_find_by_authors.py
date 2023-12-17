import sys
import os

sys.path.append(os.path.join(os.getcwd(), "src"))


from src.main import find_by_authors
from src.seed import seed_authors_from_json


def find_by_authors_exist_in_db():
    seed_authors_from_json()
    assert find_by_authors("er") == {
        "Albert Einstein": [
            "“The world as we have created it is a process of our "
            "thinking. It cannot be changed without changing our "
            "thinking.”",
            "“There are only two ways to live your life. One is as "
            "though nothing is a miracle. The other is as though "
            "everything is a miracle.”",
            "“Try not to become a man of success. Rather become a man " "of value.”",
            "“The world as we have created it is a process of our "
            "thinking. It cannot be changed without changing our "
            "thinking.”",
            "“There are only two ways to live your life. One is as "
            "though nothing is a miracle. The other is as though "
            "everything is a miracle.”",
            "“Try not to become a man of success. Rather become a man " "of value.”",
        ]
    }


def find_by_authors_not_exist_in_db():
    assert find_by_authors("sp") == []
