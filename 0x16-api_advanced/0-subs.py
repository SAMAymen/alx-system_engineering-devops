import requests

#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    try:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
        }
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        results = response.json().get("data")
        return results.get("subscribers")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0
