import sqlite3
import requests
from bs4 import BeautifulSoup
import pandas as pd

def largest_banks(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})
    data = [header.text.strip() for header in table.find_all('th')]
    rows = []
    for row in table.find_all('tr')[1:]:
        cells = [cell.text.strip() for cell in row.find_all('td')]
        rows.append(cells)

    df = pd.DataFrame(rows, columns=data)
    df[data[2]] = df[data[2]].str.replace(',', '').astype(float)

    exchange_rate_data = {'Currency': ['EUR', 'GBP', 'INR'], 'Rate': [0.93, 0.8, 82.95]}
    df_exchange_rate = pd.DataFrame(exchange_rate_data)
    inr_exchange_rate = df_exchange_rate[df_exchange_rate['Currency'] == 'INR']['Rate'].values[0]
    gbp_exchange_rate = df_exchange_rate[df_exchange_rate['Currency'] == 'GBP']['Rate'].values[0]
    eur_exchange_rate = df_exchange_rate[df_exchange_rate['Currency'] == 'EUR']['Rate'].values[0]

    df['Market Cap (INR billion)'] = df[data[2]] * inr_exchange_rate
    df['Market Cap (EUR billion)'] = df[data[2]] * eur_exchange_rate
    df['Market Cap (GBP billion)'] = df[data[2]] * gbp_exchange_rate

    csv_path = 'C:/Users/A Sattar/Documents/largest_banks.csv'
    df.to_csv(csv_path, index=False)
    print(df)
    try:
        con = sqlite3.connect('largest_banks.db')
        print('Connection established')
        df.to_sql('banks', con, if_exists='replace', index=False)
        con.commit()
        print('Table created successfully')

        cursor = con.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='banks';")
        if cursor.fetchone():
            print('Table "banks" exists in the database')
        else:
            print('Table "banks" does NOT exist in the database')
    except Exception as e:
        print(f"Error: {e}")
    finally:
        con.close()

    try:
        conn = sqlite3.connect('largest_banks.db')
        curs = conn.cursor()
        query = 'SELECT * FROM banks'
        curs.execute(query)
        rows = curs.fetchall()
        print(rows)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()


path = 'https://web.archive.org/web/20230908091635/https:/en.wikipedia.org/wiki/List_of_largest_banks'
largest_banks(path)