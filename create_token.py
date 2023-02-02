import requests

def get_long_lived_token(short_lived_token):
    # Construct the URL to exchange the short-lived token
    url = f"https://graph.facebook.com/v12.0/oauth/access_token?grant_type=fb_exchange_token&client_id={APP_ID}&client_secret={APP_SECRET}&fb_exchange_token={short_lived_token}"

    # Make the request to exchange the token
    response = requests.get(url)

    # Extract the long-lived token from the response
    long_lived_token = response.json()["access_token"]

    # Print the long-lived token
    print("Long-lived token: ")
    print(long_lived_token)
