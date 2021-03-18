from bs4 import BeautifulSoup
import os
import urllib.request
import urllib

url =  'https://vnexpress.net'


nofeed = 0
minFeed = 1000 

def save_data(idx_page):
  global nofeed
  
  crawl_link = "{}/{}-p{}".format(url, topic, idx_page)
  page = urllib.request.urlopen(crawl_link)
  soup = BeautifulSoup(page, 'html.parser')
  feeds = soup.findAll(class_='item-news-common')


  for npfeed in feeds:
    nfeed = npfeed.find(class_='title-news') 
    if nfeed==None:
      continue
    feed = nfeed.find("a")
    title = feed.get('title')
    link = feed.get('href')
    description = npfeed.find(class_='description').find("a").text

    if title==None or title=="" or link==None or description=="":
      continue
    
    fname = ''.join(e for e in title if e.isalnum())
    file_uri = "{}\{}.txt".format(file_dir, fname)
    
    print('Title: {} - Link: {}'.format(title, link))
    with open(file_uri,"w", encoding="utf-8") as f:
      f.write(title)
      f.write("\n")
      f.write(link)
      f.write("\n")
      f.write(description)
      f.write("\n")
      txt = crawl_news(link)    
      f.write(txt)
    f.close() 
    print("Crawled feed {} - page {}".format(nofeed, idx_page))
    nofeed+=1
def crawl_news(url):
  page = urllib.request.urlopen(url)
  soup = BeautifulSoup(page, 'html.parser')
  
  fck_detail = soup.find(class_="fck_detail")
  if fck_detail == None:
    return ""
  paras = fck_detail.findAll(class_="Normal", attrs={'style': ''})
  txt = ""
  for para in paras:
    for part in para.contents:
      txt +=str(part)
    txt +="\n"

  # print(txt)
  return txt


with open("topics.txt", "r") as reader:
  
  topic_list = reader.read().splitlines()
  for topic in topic_list:
    nofeed = 0
    file_dir = os.getcwd() + "\\data\\" + topic

    if not os.path.exists(file_dir):
      os.makedirs(file_dir)
      
    idx_page = 1
    while nofeed < minFeed:
      # log start craw topic      
      fname = "{}/log.txt".format(file_dir)
      with open(fname,"w+", encoding="utf-8") as f:
        f.write("- Start crawl items {} - page {}".format(topic, idx_page))
        f.close()
      
      save_data(idx_page)
      idx_page+=1
    

# crawl_news("https://vnexpress.net/canh-dong-hoa-tren-san-thuong-cua-nguoi-phu-nu-ha-noi-4215292.html");
print (str(nofeed) + " items")