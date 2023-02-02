import requests

def get_long_lived_token(short_lived_token):
    # Construct the URL to exchange the short-lived token
    # Replace APP_ID and APP_SECRET with the corresponding values of your Facebook app
    url = f"https://graph.facebook.com/v12.0/oauth/access_token?grant_type=fb_exchange_token&client_id={APP_ID}&client_secret={APP_SECRET}&fb_exchange_token={short_lived_token}"

    # Make the request to exchange the token using the requests library
    response = requests.get(url)

    # Extract the long-lived token from the response
    # The response is in JSON format, and the long-lived token is in the 'access_token' field
    long_lived_token = response.json()["access_token"]

    # Return the long-lived token
 
    print("Long-lived token: ")
    print(long_lived_token)
