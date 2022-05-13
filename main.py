import nasdaqdatalink as quandl
import smtplib
import boto3
import pandas as pd

quandl.ApiConfig.api_key = 'Api key'
data = quandl.get('ECONOMIST/BIGMAC_ROU', start_date='2021-07-31', end_date='2021-07-31')

print(data)

data_frame = pd.DataFrame(data)
data_frame.to_csv('Demo3.csv')

s3 = boto3.client('s3')
s3.upload_file('D:/Onwelo/Demo3.csv', 'pandasv2', 'Demo3.csv')

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login('email', '***************')

server.sendmail('email', 'katarzyna.pieta@onwelo.com', 'Hi, it is Daniil Boika, data was upload to S3')

print('Mail sent')