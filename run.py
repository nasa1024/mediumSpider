import requests
from bs4 import BeautifulSoup
import json
import time
import re

def get_user_id(username):
    pattern = re.compile(r'{"__ref":"User:(.*?)"}')
    user_url = f'https://medium.com/@{username}'
    user_page = requests.get(user_url)
    user_id = pattern.findall(user_page.text)[0]
    return user_id

def get_author_articles(user_id, username):
    base_url = 'https://medium.com/_/api/users/{user_id}/profile/stream?limit=10&to={timestamp}'
    all_articles = []
    latest_timestamp = int(time.time() * 1000)

    while True:
        url = base_url.format(user_id=user_id, timestamp=latest_timestamp)
        headers = {'Accept': 'application/json'}
        response = requests.get(url, headers=headers)
        try:
            data = json.loads(response.text[16:])
            posts = data.get('payload', {}).get('references', {}).get('Post', {})
            if not posts:
                break
            for post_id, post_data in posts.items():
                article = {
                    'id': post_id,
                    'title': post_data['title'],
                    'url': f'https://medium.com/{username}/{post_data["uniqueSlug"]}',
                    'publishedAt': post_data['firstPublishedAt']
                }
                all_articles.append(article)
        except Exception as e:
            print(e)
            break

        latest_timestamp = all_articles[-1]['publishedAt'] - 1

    return all_articles

def get_article_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    title = soup.find('h1').get_text()
    content = "\n".join(p.get_text() for p in paragraphs)
    return title,content

if __name__ == "__main__":
    author_username = 'author_username' # 作者的用户名
    user_id = get_user_id(author_username)

    articles = get_author_articles("user_id", author_username)
    print(f"Total articles: {len(articles)}")
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"URL: {article['url']}")
        title,content = get_article_content(article['url'])
        print("Content:")
        print(content)
        print("Title:")
        print(title)
        print("\n---\n")