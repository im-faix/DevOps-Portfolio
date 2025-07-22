import requests
import json
import os

GITHUB_USERNAME = "im-faix"  # Replace with your username
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")  # Use GitHub secret
TOPIC = "devops"

def get_repos():
    url = f"https://api.github.com/search/repositories?q=user:{GITHUB_USERNAME}+topic:{TOPIC}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    repos_data = []
    for repo in data.get("items", []):
        repos_data.append({
            "id": repo["id"],
            "name": repo["name"],
            "description": repo["description"],
            "html_url": repo["html_url"]
        })

    with open("client/public/repos.json", "w") as f:
        json.dump(repos_data, f, indent=2)

if __name__ == "__main__":
    get_repos()
