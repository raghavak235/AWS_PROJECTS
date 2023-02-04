import os

import boto3
import yfinance as yf

client = boto3.client("s3")


def stocks_data_csv(stock_name):
    # Getting the stock data
    stock_data = yf.download(stock_name, start='2010-01-01', end='2022-01-01')
    stock_data.to_csv(stock_name+'.csv')


def uploading_s3(stock_name, bucket_name):

    try:
        client.upload_file(stock_name+'.csv', bucket_name, stock_name+'.csv')
    except Exception as e:
        print(e)
    else:
        os.remove(stock_name+'.csv')


if __name__ == '__main__':
    stock_name = 'TSLA'
    bucket_name = 's3uploadtestinginput'
    stocks_data_csv(stock_name)
    uploading_s3(stock_name, bucket_name)