#encoding=utf-8

import requests
import logging

import json
from os import makedirs
from os.path import exists

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s: %(message)s')
INDEX_URL = 'https://dynamic1.scrape.cuiqingcai.com/api/movie/?limit={limit}&offset={offset}'

def scrape_api(url):
    logging.info("scraping %s", url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)

LIMIT = 10

def scrape_index(page):
    url = INDEX_URL.format(limit=LIMIT, offset=LIMIT * (page - 1))
    return scrape_api(url)

DETAIL_URL = 'https://dynamic1.scrape.cuiqingcai.com/api/movie/{id}'

def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    return scrape_api(url)

TOTAL_PAGE = 10
RESULTS_DIR = 'results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.json'
    json.dump(data, open(data_path,'w',encoding='utf-8'), ensure_ascii=False, indent=2)

# 这里我们定义了一个 main 方法，首先遍历获取页码 page，然后把 page 当成参数传递给 scrape_index 方法，
# 得到列表页的数据。接着我们遍历所有列表页的结果，获取每部电影的 id，然后把 id 当作参数传递给 scrape_detail 方法，
# 来爬取每部电影的详情数据，赋值为 detail_data，输出即可。
def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_data = scrape_index(page)
        for item in index_data.get('results'):
            id = item.get('id')
            detail_data = scrape_detail(id)
            logging.info("detail data %s", detail_data)
            save_data(detail_data)

if __name__ == '__main__':
    main()