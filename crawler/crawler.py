from bs4 import BeautifulSoup
import urllib.request
import json
from newspaper import Article


def page_crawl(link, title, topic):
    news = {}
    news["title"] = title
    news['topic'] = topic
    url = "https://dantri.com.vn" + str(link)
    news["url"] = url
    article = Article(url)
    article.download()
    article.parse()
    content = article.text
    news["content"] = content
    return news


def crawl(topic):
    result = []
    print(topic)
    for i in range(30):
        url = "https://dantri.com.vn/{}/trang-{}.htm".format(topic, i)
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, "html.parser")
        new_feeds = soup.findAll(class_="news-item__title")

        for nfeed in new_feeds:
            feed = nfeed.find("a")
            title = feed.get("title")
            link = feed.get("href")
            if link == None:
                continue
            result.append(page_crawl(link, title, topic))  
    return result


topics = [
    "su-kien",
    "xa-hoi",
    "the-gioi",
    "the-thao",
    "lao-dong-viec-lam",
    "suc-khoe",
    "tam-long-nhan-ai",
    "kinh-doanh",
    "giao-duc-huong-nghiep",
    "van-hoa",
]
__result = []
for topic in topics:
    crawler = crawl(str(topic))
    __result.extend(crawler)
with open("./new/data.json".format(str(topic)), "w+", encoding="utf8") as f:
    json.dump(__result, f,  indent=4, ensure_ascii=False)
f.close()
