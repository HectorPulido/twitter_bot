import json
from twitter_data.models import User, Features


def run():
    users_to_delete = "USERS_TO_DELETE"
    users_to_delete_data = {"min_retweets": 5, "count": 1000}

    users_to_follow = "USERS_TO_FOLLOW"
    users_to_follow_data = {"min_retweets": 5, "min_retweets_to_like": 10}

    tweets_to_delete = "TWEETS_TO_DELETE"
    tweets_to_delete_data = {"count": 1000}

    Features.objects.create(
        name=users_to_delete, value=json.dumps(users_to_delete_data)
    )
    Features.objects.create(
        name=users_to_follow, value=json.dumps(users_to_follow_data)
    )
    Features.objects.create(
        name=tweets_to_delete, value=json.dumps(tweets_to_delete_data)
    )