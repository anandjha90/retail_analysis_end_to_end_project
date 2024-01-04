PRE-REQUISITE:

pip install numpy
pip install pandas
pip install pandas_profiling
pip install seaborn
pip install jupyter_scheduler
pip install jupyterlab-scheduler
pip install snowflake-connector-python
pip install snowflake-sqlalchemy
pip install "snowflake-connector-python[pandas]"


import numpy as np
import pandas as pd
import pandas_profiling 
import matplotlib.pyplot as plt 
import getpass
import seaborn as sns 
%matplotlib inline
import snowflake.connector

conn = snowflake.connector.connect(
        user = 'YOUR USERNAME',
        password = getpass.getpass('Your Snowflake Password: '),
        ##password='Your password',
        ##  account = https://bpbqkgp-qd32415.snowflakecomputing.com
        account = 'bpbqkgp-qd32415',
        database='RETAILS',
        schema='PUBLIC',
        warehouse='COMPUTE_WH',
  ) 
  
cur = conn.cursor()
  
select_demographic_RAW = 'SELECT * FROM demographic_RAW'
select_CAMPAIGN_DESC_RAW = 'SELECT * FROM CAMPAIGN_DESC_RAW'
select_CAMPAIGN_RAW = 'SELECT * FROM CAMPAIGN_RAW'
select_PRODUCT_RAW = 'SELECT * FROM PRODUCT_RAW'
select_COUPON_RAW = 'SELECT * FROM COUPON_RAW'
select_COUPON_REDEMPT_RAW = 'SELECT * FROM COUPON_REDEMPT_RAW'
select_TRANSACTION_RAW = 'SELECT * FROM TRANSACTION_RAW'

cur.execute(select_demographic_RAW)
demographic_RAW = cur.fetch_pandas_all()

cur.execute(select_CAMPAIGN_DESC_RAW)
CAMPAIGN_DESC_RAW = cur.fetch_pandas_all()

cur.execute(select_CAMPAIGN_RAW)
CAMPAIGN_RAW = cur.fetch_pandas_all()

cur.execute(select_PRODUCT_RAW)
PRODUCT_RAW = cur.fetch_pandas_all()

cur.execute(select_COUPON_RAW)
COUPON_RAW = cur.fetch_pandas_all()

cur.execute(select_COUPON_REDEMPT_RAW)
COUPON_REDEMPT_RAW = cur.fetch_pandas_all()

cur.execute(select_TRANSACTION_RAW)
TRANSACTION_RAW = cur.fetch_pandas_all()

cur.close()
conn.close()

demographic_RAW.head(5)
CAMPAIGN_DESC_RAW.head(5)
CAMPAIGN_RAW.head(5)
PRODUCT_RAW.head(5)
COUPON_RAW.head(5)
COUPON_REDEMPT_RAW.head(5)
TRANSACTION_RAW.head(5)