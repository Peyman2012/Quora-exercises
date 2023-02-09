import request
response = requests.get('https://www.boredapi.com/api/activity?type=education')
print("Start a webinar on a topic of your choice:",response)