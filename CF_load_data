import asyncio
import nest_asyncio
from cod_api import API, platforms

# Initiate the API class
api = API()

# Allow nested use of asyncio.run() in Jupyter Notebook
nest_asyncio.apply()

async def example():
    # Log in with the SSO token
    await api.loginAsync('')

    # Retrieve combat history
    hist = await api.Warzone.combatHistoryAsync(platforms.Activision, "RIDbrud#8174385")  # Returns data of type dict

    # Print results to the console
    print(hist)

# Run the asynchronous code using asyncio.run()
asyncio.run(example())
