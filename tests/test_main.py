import sys
import os
import pytest

sys.path.append(os.path.join(os.getcwd(), "src"))

from src.main import parse_user_input, handler
from src.main import find_by_tag, find_by_authors, find_by_tags

# from src.seed import delete_collections, seed_authors_from_json, seed_qoutes_from_json
# from src.models import Author, Quote


@pytest.mark.parametrize(
    "user_input, parser_command, parser_parameters",
    [
        ("name: Steve Martin", "name", ["Steve Martin"]),  # True
        ("tag: live", "tag", ["live"]),  # True
        ("TAG: live", "tag", ["live"]),
        ("tag: live", "tag", ["live"]),
        ("tags: live,life", "tags", ["live", "life"]),
        ("exit", "exit", []),
        ("", "_", None),
    ],
)
def test_parse_user_input(user_input, parser_command, parser_parameters):
    command, parameters = parse_user_input(user_input)
    assert command == parser_command
    assert parameters == parser_parameters


@pytest.mark.parametrize(
    "command, parameters, expect_result",
    [
        (
            "name",
            ["Steve Martin"],
            {"Steve Martin": ["“A day without sunshine is like, you know, night.”"]},
        ),  # True
        (
            "name",
            ["Albert Einstein"],
            {
                "Albert Einstein": [
                    "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”",
                    "“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”",
                    "“Try not to become a man of success. Rather become a man of value.”",
                ]
            },
        ),
        (
            "tag",
            ["live"],
            [
                "“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”"
            ],
        ),
        (
            "tag",
            ["python"],
            [],
        ),
        (
            "exit",
            [],
            "exit",
        ),
        (
            "_",
            [],
            "Wrong command. Try again",
        ),
    ],
)
def test_handler(command, parameters, expect_result):
    result = handler(command, parameters)
    assert result == expect_result


@pytest.mark.parametrize(
    "tag, expect_result",
    [
        (
            "live",
            [
                "“There are only two ways to live your life. One is as though nothing is a "
                "miracle. The other is as though everything is a miracle.”"
            ],
        ),
        (
            "li",
            [
                "“There are only two ways to live your life. One is as though nothing is a "
                "miracle. The other is as though everything is a miracle.”"
            ],
        ),
        (
            "world",
            [
                "“The world as we have created it is a process of our thinking. It cannot be "
                "changed without changing our thinking.”"
            ],
        ),
        (
            "wo",
            [
                "“The world as we have created it is a process of our thinking. It cannot be "
                "changed without changing our thinking.”"
            ],
        ),
    ],
)
def test_find_by_tag(tag, expect_result):
    result = find_by_tag(tag)
    assert result == expect_result


@pytest.mark.parametrize(
    "tags, expect_result",
    [
        (
            ["live"],
            [
                "“There are only two ways to live your life. One is as though nothing is a "
                "miracle. The other is as though everything is a miracle.”"
            ],
        ),
        (
            ["world"],
            [
                "“The world as we have created it is a process of our thinking. It cannot be "
                "changed without changing our thinking.”"
            ],
        ),
        (
            ["live", "world"],
            [
                "“There are only two ways to live your life. One is as though nothing is a "
                "miracle. The other is as though everything is a miracle.”",
                "“The world as we have created it is a process of our thinking. It cannot be "
                "changed without changing our thinking.”",
            ],
        ),
    ],
)
def test_find_by_tags(tags, expect_result):
    result = find_by_tags(tags)
    assert result == expect_result
