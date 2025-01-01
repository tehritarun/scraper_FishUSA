from curl_cffi import requests
from models import JSONResponseModel
import logging
from rich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(
    level="INFO", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)
log = logging.getLogger("rich")


def create_session():
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,hi;q=0.8,pa;q=0.7,id;q=0.6',
        'origin': 'https://www.fishusa.com',
        'priority': 'u=1, i',
        'referer': 'https://www.fishusa.com/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    session = requests.Session()
    session.headers.update(headers)
    return session


def api_request(session: requests.session, url: str, page: int):
    params = {
        'userId': '2813077d-ed04-408f-a3e9-1389bde0ff0a',
        'domain': 'https://www.fishusa.com/fishing-rods-reels/?view=products&p=2',
        'sessionId': '20cce876-5f8a-442e-8d9f-6b09010d1a4f',
        'pageLoadId': '2d74cc1d-0c64-47e3-a54e-92901c255d5d',
        'siteId': 'vw1136',
        'page': str(page),
        'bgfilter.custom_ss_hide': 'N',
        'bgfilter.categories_hierarchy': 'Rods & Reels',
        'redirectResponse': 'full',
        'ajaxCatalog': 'Snap',
        'resultsFormat': 'native',
    }

    response = session.get(
        url, params=params)

    log.info(response.status_code)

    try:
        return JSONResponseModel(**response.json())
    except Exception as e:
        log.error(e)
        return JSONResponseModel()


def main():
    url = 'https://vw1136.a.searchspring.io/api/search/search.json'
    session = create_session()
    page_resp = api_request(session, url, 1)
    if page_resp.pagination is None:
        raise Exception("no pages found")

    lastpage = page_resp.pagination.totalPages
    for page in range(1, lastpage+1):
        response = api_request(session, url, page)
        log.info(response.pagination)
        if response.results is None:
            log.info("no results found")
        else:
            for result in response.results:
                log.info(result.name)


if __name__ == "__main__":
    main()
