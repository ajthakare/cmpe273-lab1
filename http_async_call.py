import aiohttp
import asyncio
import requests
import random

print("\nLab 1 Assingment 2\nAsynchronous calls for HTTP Request\n")

webhookpath="https://webhook.site/e2eb4553-8b8e-46da-b7f5-17551fee7f9e"

#asynchronous code using aiohttp below

async def print_http_response(i):
    async with aiohttp.ClientSession() as session:
        async with session.get(webhookpath) as response:
            #print(response.status)
            print("Response "+str(i)+" Date- "+response.headers['date'])

#asynchronous code using asyncio below

# async def print_http_response(i):
#     response = requests.get(webhookpath)
#     sleeptime=random.randint(1,3)
#     await asyncio.sleep(sleeptime)
#     if(response.status_code==requests.codes.ok):
#         print("Response "+str(i)+" Date- "+response.headers['date'])
#         #print("(Slept for "+str(sleeptime)+" secs)")
#     else:
#         response.raise_for_status()
#         print("Error occured for request number "+str(i))
            

responses=[]
for i in range(3):
    responses.append(asyncio.ensure_future(print_http_response(i+1)))
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(responses))
loop.close()