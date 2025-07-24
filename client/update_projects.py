import requests
import os

USERNAME = "im-faix"
TOKEN = os.getenv("GH_TOKEN")
README_PATH = "README.md"
START = "<!--PROJECTS_START-->"
END = "<!--PROJECTS_END-->"

def get_devops_repos():
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.mercy-preview+json"
    }
    url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&sort=updated"
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    repos = res.json()
    return [repo for repo in repos if "devops" in repo.get("topics", [])]

def format_repo(repo):
    return f"- 🔗 [{repo['name']}]({repo['html_url']}): {repo['description'] or 'No description'}"

def update_readme(repos):
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    start = content.find(START) + len(START)
    end = content.find(END)
    new_section = "\n" + "\n".join(format_repo(r) for r in repos[:5]) + "\n"
    new_content = content[:start] + new_section + content[end:]
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    devops_repos = get_devops_repos()
    update_readme(devops_repos)
