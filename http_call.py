
import requests

print("\nLab 1 Assignment 1\nSynchronous calls to HTTP Request\n")

webhookpath="https://webhook.site/e2eb4553-8b8e-46da-b7f5-17551fee7f9e"


for i in range(3):
    response = requests.get(webhookpath)
    if(response.status_code==requests.codes.ok):
        print("Response "+str(i+1)+" Date- "+response.headers['date'])
    else:
        print("Error occured for request number "+str(i+1))
