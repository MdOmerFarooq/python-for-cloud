import requests   # importing requests module

url = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'  

pull_data = requests.get(url) # api to fetch data from repo kubernetes/kubernetes/pulls

if pull_data.status_code == 200 :  # if the API is good and data is returned
    pull_data= pull_data.json()    # convert the data into dict and store in pulldata
    usernames = {}                 # empty dict to store the usernames and count
    for i in pull_data:
        user = i["user"]['login']
        if user in usernames:
            usernames[user] += 1    # key is username and its value is count 
        else :
            usernames[user] = 1
    print(usernames)
else :
    print(f'error fetching data {pull_data.status_code}')   




