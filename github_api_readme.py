import requests

# Get the API URL for the scikit-learn repository
url = "https://api.github.com/repos/scikit-learn/scikit-learn/readme"

# Make a request to the API
response = requests.get(url)

# Check the response status code
if response.status_code == 200:
    # The request was successful, so get the README
    read_me = response.json()

    # Print the README
    print(read_me)
else:
    # The request failed, so print the error message
    print(response.status_code, response.reason)