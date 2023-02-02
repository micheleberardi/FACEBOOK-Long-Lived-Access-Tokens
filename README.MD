# FACEBOOK-Long-Lived-Access-Token

Here's an example of how to obtain a long-lived access token in Python using the Facebook Graph API:

```
import requests

def get_long_lived_token(short_lived_token):
    # Construct the URL to exchange the short-lived token
    url = f"https://graph.facebook.com/v12.0/oauth/access_token?grant_type=fb_exchange_token&client_id={APP_ID}&client_secret={APP_SECRET}&fb_exchange_token={short_lived_token}"

    # Make the request to exchange the token
    response = requests.get(url)

    # Extract the long-lived token from the response
    long_lived_token = response.json()["access_token"]

    return long_lived_token
```

In this example, APP_ID and APP_SECRET should be replaced with the corresponding values of your Facebook app. The get_long_lived_token function takes a short-lived token as input and returns a long-lived token. The function makes a request to the Facebook Graph API to exchange the short-lived token for a long-lived token. The response is in JSON format, and the long-lived token is extracted from the access_token field.
