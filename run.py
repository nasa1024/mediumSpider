import requests
from bs4 import BeautifulSoup
import json
import time

def get_user_id(username):
    user_url = f'https://medium.com/@{username}'
    user_page = requests.get(user_url)
    soup = BeautifulSoup(user_page.content, 'html.parser')
    user_id = None

    for script in soup.find_all('script'):
        if 'preloaded' in str(script):
            preloaded_data = json.loads(str(script.contents[0])[str(script.contents[0]).find('{'):])
            user_id = preloaded_data['payload']['user']['userId']
            break
    print(soup)
    # // 保存到本地
    with open('user_id.txt', 'w') as f:
        f.write(user_page.text)


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
    content = "\n".join(p.get_text() for p in paragraphs)
    return content

if __name__ == "__main__":
    author_username = 'jiamigou'
    # user_id = get_user_id(author_username)

    articles = get_author_articles("dc71f53b5d42", author_username)
    print(f"Total articles: {len(articles)}")
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"URL: {article['url']}")
        # content = get_article_content(article['url'])
        # print("Content:")
        # print(content)
        print("\n---\n")