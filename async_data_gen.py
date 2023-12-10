import datetime
import requests
import asyncio
import aiohttp


async def fetch_url(session, url, params, ret_dict):
    async with session.get(url=url, params=params) as response:
        res = await response.text()
        res = list(map(lambda x: x.replace('"', ''), res[2:-2].split(',')))
        res[11] = '0'
        ret_dict[params["X"]] = res[:12]


async def main():
    ret_dict = {}
    urls = []
    url = "https://YOUR_URL"
    with open("X", "r") as file:
        for x in file:
            params = {"X": x[:-1].upper(), "X": "X", "X": 2}
            urls.append([url, params])
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url, params, ret_dict) for url, params in urls]
        await asyncio.gather(*tasks)

    return ret_dict


def send_request(request):
    url = 'http://YOUR_URL'
    YOUR_DB_user = 'YOUR_USER'
    YOUR_DB_password = 'YOUR_PASSWORD'

    auth = (YOUR_DB_user, YOUR_DB_password)
    requests.post(url=url, auth=auth, data=request)


def get_x():
    url = 'http://YOUR_URL'
    YOUR_DB_user = 'YOUR_USER'
    YOUR_DB_password = 'YOUR_PASSWORD'
    request = "select YOUR_SQL_REQ"
    auth = (YOUR_DB_user, YOUR_DB_password)
    params = {'query': request}
    result = requests.post(url=url, auth=auth, params=params)

    return result.text


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    x = loop.run_until_complete(main())
    insert_request = "insert YOUR_SQL_REQ"
    x = get_x()[:-5]
    for x, x in x.items():
        x, x, x, x, x, x, x, x, x, x, x, x = x
        x = datetime.datetime.utcfromtimestamp(int(x) / 1000)
        if str(x) != x:
            sub_request = f"YOUR_VALUES"
            x += x
    send_request(x)
