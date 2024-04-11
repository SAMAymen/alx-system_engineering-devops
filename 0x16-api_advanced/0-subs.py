#!/usr/bin/python3

"""Function to query subscribers on a given Reddit subreddit."""

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            results = response.json().get("data")
            if results:
                return results.get("subscribers", 0)
            else:
                return 0
        except (KeyError, TypeError):
            # Handle the case where the response data is not in the expected format
            return 0
    elif response.status_code == 404:
        # Handle the case where the subreddit doesn't exist
        return 0
    else:
        # Handle other response status codes
        return 0