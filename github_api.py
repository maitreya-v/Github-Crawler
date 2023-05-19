import requests
import json
import transformers


url = "https://api.github.com/repos/scikit-learn/scikit-learn/commits"


# Make a request to the API.
response = requests.get(url)
# Check the response status code.
if response.status_code == 200:
    print(response)


else:
    # The request failed.
    print(response.status_code, response.reason)
# Get the commits.
commits = response.json()
# Get the latest commit.
latest_commit = commits[0]
print("This is the commit")
print(latest_commit["commit"]["message"])
# Get the commit message.
commit_message = latest_commit["commit"]["message"]


# Check if the commit message contains the word "feature".
if "feature" in commit_message:
    print("YES there is a feature")
else:
    print()
    # The commit message does not contain the word "feature", so do nothing.

# Get the LLM.
model = transformers.AutoModelForSeq2SeqLM.from_pretrained("bard")


# Generate the new section.
new_section = model.generate(
    text="## New Feature\n\n**Name:** {} \n\n**Description:** {} \n\n**Date:** {}".format(
        latest_commit["committer"]["name"], latest_commit["message"], latest_commit["committer"]["date"]
    ),
    max_length=100,
    temperature=0.7,
    top_p=0.9,
)


print("This is a new section\n")
print(new_section)