import pandas as pd
import numpy as np
import requests


def get_request(request):
    url = 'http://YOUR_URL'
    YOUR_DB_user = 'YOUR_USER'
    YOUR_DB_password = 'YOUR_PASSWORD'

    auth = (YOUR_DB_user, YOUR_DB_password)
    params = {'query': request}
    result = requests.post(url=url, auth=auth, params=params)
    if result.status_code != 200:
        print(result.status_code)

    return result.text.split('\n')


def df_creator():
    x = ['X']
    x = ['X']
    df_head = pd.DataFrame([], columns=['YOUR_COLS_LIST'])
    for x in x:
        select_request = f"select YOUR_SQL_REQ"
        x = get_request(select_request)[:-1]
        x = list(map(lambda x: x.split('\t'), x))
        df_body = pd.DataFrame(x, columns=['YOUR_COLS_LIST'])
        df_head = pd.concat([df_head, df_body])

    return df_head


def x_data_gen(x, x, x, x):
    df = pd.DataFrame([], columns=['YOUR_COLS_LIST'])
    x = ['YOUR_VALUES']
    select_request = f"select YOUR_SQL_REQ"
    res = get_request(select_request)[0]
    x = int(res) * -1 if res != '' else 0
    for x in x:
        x = x - x if x <= x else -1
        x = np.NaN
        if x > -1:
            select_request = f"select YOUR_SQL_REQ"
            x = get_request(select_request)
            x = float(x[0].split('\t')[1])
        x = (x - float(x)) / float(x) * 100.0 if x != np.NaN else np.NaN
        x = ['YOUR_DATA_LIST']
        df.loc[len(df)] = x

    return df


def csv_gen():
    df = df_creator()
    base_df = pd.DataFrame([], columns=['YOUR_COLS_LIST'])
    for x, x, x, x in zip(df['X'].items(), df['X'].items(), df['X'].items(), df['X'].items()):
        x, x, x, x = list(map(lambda x: x[1] if x is not np.NaN else x, [YOUR_LIST]))
        new_df = x_gen(x, x, x, x)
        print(new_df)
        base_df = pd.concat([base_df, new_df])
    base_df.to_csv("x.csv", index=False)


def csv_handle():
    with open("x.csv", "r") as file:
        for index, line in enumerate(file):
            if index > 0:
                print(line.split(','))


csv_gen()
