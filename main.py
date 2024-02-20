from bs4 import BeautifulSoup
import requests


def get_most_upvoted_article(url):
    """
  This function scrapes the given URL and returns the article with the most upvotes.

  Args:
    url: The URL of the webpage to scrape.

  Returns:
    A dictionary containing the title, upvotes, and link of the most upvoted article.
  """

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all articles and their corresponding links and upvotes in single loop
    articles = soup.find_all("span", class_="titleline")
    links = [a.find("a") for a in articles]
    upvotes = [int(span.text.split()[0]) for span in soup.find_all("span", class_="score")]

    # Find the index of the article with the most upvotes
    most_upvoted_index = max(range(len(upvotes)), key=upvotes.__getitem__)

    # Extract and return relevant information
    return {
        "title": articles[most_upvoted_index].text.strip(),
        "upvotes": upvotes[most_upvoted_index],
        "link": links[most_upvoted_index]["href"],
    }


# Get the most upvoted article on Hacker News
most_upvoted_article = get_most_upvoted_article("https://news.ycombinator.com/")

# Print the information
print(
    f"{most_upvoted_article['title']}, {most_upvoted_article['upvotes']} points, available at: {most_upvoted_article['link']}.")
