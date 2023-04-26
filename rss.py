import feedparser
from string import Template

# 读取 HTML 模板
with open("template.html", "r") as f:
    template = Template(f.read())
    
# 将RSS的URL传递给feedparser函数来获取数据
rss_url = "https://medium.com/feed/@jiamigou"
feed = feedparser.parse(rss_url)

# 构建 HTML 页面
items = []
for entry in feed.entries:
    item = f"<h2><a href='{entry.link}'>{entry.title}</a></h2>"
    if 'media_content' in entry:
        item += f"<img src='{entry.media_content[0]['url']}' alt='Image'/>"
    item += f"<p>{entry.summary}</p>"
    items.append(item)

html = template.safe_substitute(title=feed.feed.title, items="\n".join(items))

# 输出 HTML 页面到文件
with open("output.html", "w") as f:
    f.write(html)

