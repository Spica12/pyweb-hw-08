import redis
from redis_lru import RedisLRU
from models import Author, Quote
from pprint import pprint

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def find_by_tag(tag: str) -> list[str | None]:
    print(f"Finding by {tag}")
    quotes = Quote.objects(tags__iregex=tag)
    result = [quote.quote for quote in quotes]

    return result


@cache
def find_by_authors(author: str) -> list[str | None]:
    print(f"Finding by {author}")
    authors = Author.objects(fullname__iregex=author)
    result = {}
    for author in authors:
        quotes = Quote.objects(author=author)
        result[author.fullname] = [quote.quote for quote in quotes]

    return result


if __name__ == "__main__":
    pprint(find_by_tag("li"))
    pprint(find_by_tag("li"))

    pprint(find_by_authors("er"))
    pprint(find_by_authors("er"))

    quotes = Quote.objects().all()
    pprint([quote.to_json() for quote in quotes])
