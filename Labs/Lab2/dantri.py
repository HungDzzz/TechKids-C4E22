# pip install beautifulsoup4
# 1. dowload webpage
from urllib.request import urlopen
from bs4 import BeautifulSoup # de dung ROI
import pyexcel
from collections import OrderedDict
url = "https://dantri.com.vn"

# 1.1 connect to website
conn = urlopen(url)

# 1.2 dowload raw data (data tho)
raw_data = conn.read()

# 1.3 decode data (decode ra utf-8)
webpage_text = raw_data.decode("utf-8")

#print(len(webpage_text))
# 1.4 Save text
    # w = write , b = binary (data thô)
    ##f = open("dantri.html","wb")
    ##f.write(raw_data)
    ##f.close()

# 2 extra ROI (chon vung can )
# 2.1 convert text to soup
soup = BeautifulSoup(webpage_text, "html.parser") # de danh dau la html
##print(soup.prettify()) # prettify : lam dep theo the dong the mo
ul = soup.find("ul", "ul1 ulnew") # class k can phai dan nhan khong thi phai viet day du vd : id = ...
###print(ul.prettify()) # find_all tim het
li_list = ul.find_all("li")
# for li in li_list:
#     print(li.prettify())
#     print("***********")
news_list = []
for li in li_list:
##li = li_list[0]
    h4 = li.h4
    a = h4.a
    # a = li.h4.a
    title = a.string # string laf content (giua the mo,dong)
    link = url + a["href"]
    # print(title)
    # print(link)
    new = OrderedDict({
        'Title': title,
        'Link': link
    })
    news_list.append(new)
#print(*news_list, sep = '\n')
# pip install pyexcel
# pip install pyexcel-xlxs (duoi xlxs)
# pip install pyexcel-xls (duoi xls)


# 3. extra data

# 4. save data
pyexcel.save_as(records=news_list, dest_file_name ="dantri.xls")