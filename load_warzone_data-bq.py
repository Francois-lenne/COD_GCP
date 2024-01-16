import asyncio
import nest_asyncio
from cod_api import API, platforms
import pandas as pd
from pandas import json_normalize

# Initiate the API class
api = API()

# Allow nested use of asyncio.run() in Jupyter Notebook
nest_asyncio.apply()

async def retrieve_cod_data():
    # Log in with the SSO token
    await api.loginAsync('')

    # Retrieve combat history
    hist = await api.ModernWarfare.combatHistoryAsync(platforms.Activision, "yupex#9664411")  # Returns data of type dict

    # Normalize the nested dictionary and convert it to a pandas DataFrame
    df = json_normalize(hist["data"]["matches"])

    # print(df.head())
    return df

# Run the asynchronous code using asyncio.run()
df = asyncio.run(retrieve_cod_data())

df.to_csv('warzone_data2.csv', index=False)
