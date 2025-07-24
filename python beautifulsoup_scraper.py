import requests
from bs4 import BeautifulSoup

def scrape_hockey_teams():
    url = "https://www.scrapethissite.com/pages/forms/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    teams = soup.find_all("tr", class_="team")

    for i, team in enumerate(teams, 1):
        name = team.find("td", class_="name").get_text(strip=True)
        year = team.find("td", class_="year").get_text(strip=True)
        wins = team.find("td", class_="wins").get_text(strip=True)
        losses = team.find("td", class_="losses").get_text(strip=True)

        print(f"{i}. {name} ({year})")
        print(f"   Wins: {wins} | Losses: {losses}\n")

if __name__ == "__main__":
    scrape_hockey_teams()
