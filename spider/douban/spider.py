'''
just for learning python craw.
to crawing douban's book info from page1 to page10 with multiprocessing
attention:you can start this demo in a little few times,
then douban will banned your source ip to get info from douban.
The following source URL information for the test
url =  https://www.douban.com/doulist/1264675/
'''
import re
import io
import requests
import json
from requests.exceptions import RequestException
from multiprocessing import Pool

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<div class="post">.*?src="(.*?)".*?blank">'
                         +'(.*?)</a>.*?nums">(.*?)</span>.*?abstract">(.*?)<br />(.*?)<br />(.*?)</div>', re.S)
    items = re.findall(pattern,html)
#    print(items)
    for item in items:
        yield{
            'img':item[0],
            'name':item[1].strip(),
            'score':item[2],
            'writtor':item[3].strip(),
            'publish orgnization':item[4].strip(),
            'year':item[5].strip()
        }

def write_to_file(content):
    with io.open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close

def main(offset):
    url = 'https://www.douban.com/doulist/1264675/?start='+ str(offset) +'&sort=seq&sub_type='
    html = get_one_page(url)
#    print(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)




if __name__ == '__main__':
#first page      https://www.douban.com/doulist/1264675/?start=0&sort=seq&sub_type=
#second page     https://www.douban.com/doulist/1264675/?start=25&sort=seq&sub_type=
#third page      https://www.douban.com/doulist/1264675/?start=50&sort=seq&sub_type=


#    non multiprocess get page1 to page10, you can use this to test,and don't forget to commented out pool's related info.
#
#    L = [(i-1)*25 for i in range(1,11)]
#    for offset in L:
#        main(offset)

    pool = Pool()
    pool.map(main,[(i-1)*25 for i in range(1,11)])
