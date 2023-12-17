import sys
import os

sys.path.append(os.path.join(os.getcwd(), "src"))

from src.main import find_by_tag


def test_find_by_tag_exist_in_db():
    assert find_by_tag("li") == [
        "“There are only two ways to live your life. One is as though nothing is a "
        "miracle. The other is as though everything is a miracle.”",
        "“There are only two ways to live your life. One is as though nothing is a "
        "miracle. The other is as though everything is a miracle.”",
    ]


def test_find_by_tag_not_exist_in_db():
    assert find_by_tag("as") == []
