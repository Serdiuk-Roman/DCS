

import redis

redis_db = redis.Redis('localhost', 6379)


def run_task(link):

    try:
        redis_db.lpush(
            'porter_scrap:start_urls',
            link
        )
    except Exception:
            return "Error DB"
