import requests

# curl 'https://medium.com/@jiamigou' \
#   -H 'authority: medium.com' \
#   -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
#   -H 'accept-language: zh-CN,zh;q=0.9,en;q=0.8' \
#   -H 'cache-control: max-age=0' \
#   -H 'cookie: _ga=GA1.2.1611829913.1620565272; uid=lo_7767a104c231; sid=1:W0Wx2WOAfZvpb155y1jnseclmRarYAcY3Hi7soMxBDwWPSu2O3W8PzJy4wqS1HoK; __cfruid=8414136fa48a6871a002bdf3b994155c610af7a0-1682432777; _gid=GA1.2.301994419.1682432786; _gat=1; _dd_s=rum=0&expire=1682434395529' \
#   -H 'sec-ch-ua: "Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "Windows"' \
#   -H 'sec-fetch-dest: document' \
#   -H 'sec-fetch-mode: navigate' \
#   -H 'sec-fetch-site: none' \
#   -H 'sec-fetch-user: ?1' \
#   -H 'upgrade-insecure-requests: 1' \
#   -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36' \
#   --compressed

# 获取作者所有的文章


def get_author_articles(author):
    url = 'https://medium.com/@' + author
    # set useragent
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'}
    r = requests.get(url, headers=headers)
    print(r.text)


# 爬取medium的文章


if __name__ == '__main__':
    get_author_articles('jiamigou')
