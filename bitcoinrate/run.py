import psycopg2
import requests
from environ import Env

env = Env()
env.read_env()  # read .env file, if it exists
# required variables
apikey = env("apikey")  # => 'sloria'

url='https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=' + apikey
rowData = requests.get(url)
responseData = rowData.json()
Data = responseData['Realtime Currency Exchange Rate']
exchangeRate = Data['5. Exchange Rate']
try:
    connection = psycopg2.connect(user="postgres",
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="BitcoinUSDRate")
    cursor = connection.cursor()
    postgres_select_query = """ SELECT id FROM bitcoinrate_bitcoinrate"""
    cursor.execute(postgres_select_query)

    connection.commit()
    count = cursor.rowcount
           
    postgres_insert_query = """ INSERT INTO bitcoinrate_bitcoinrate (id, rate) VALUES (%s,%s)"""
    record_to_insert = (cursor.rowcount + 1,exchangeRate)
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into rate tab le", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")