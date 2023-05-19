# release notes
import requests

# Get the list of releases for the scikit-learn repo.
response = requests.get("https://api.github.com/repos/scikit-learn/scikit-learn/releases")
list_of_releases=[]
# If the request was successful, parse the response and extract the release notes.
if response.status_code == 200:
    releases = response.json()

    # Loop over the releases and print the release notes.
    for release in releases:
        list_of_releases.append(release["name"])
        list_of_releases.append(release["body"])