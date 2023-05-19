import requests

def print_all_commit_messages():
    url = 'https://api.github.com/repos/scikit-learn/scikit-learn/commits'
    page_num = 1
    while True:
        response = requests.get(url, params={'per_page': 100, 'page': page_num})
        if response.status_code == 200:
            response_json = response.json()
            if len(response_json) == 0:
                break
            for res in response_json:
                if "Co-authored-by" in str(res):
                    continue
                else:
                    print(res["commit"]["message"])
            page_num += 1
        else:
            print("Failed to fetch commits for page", page_num)
            break
