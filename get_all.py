import requests

# Set the request parameters
url = 'https://zendeskcodingchallenge8643.zendesk.com/api/v2/tickets.json'
user = 'rstli@ucdavis.edu'+ '/token'
pwd = 'hLWJTPCI6vXxIFjGcT6XnxDpG7MnfVSehNy7RZLP'

# Do the HTTP get request
response = requests.get(url, auth=(user, pwd))

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print('length', len(data['tickets']))
'''
# Example 1: Print the name of the first group in the list
print( 'First group = ', data['groups'][0]['name'] )

# Example 2: Print the name of each group in the list
group_list = data['groups']
for group in group_list:
    print(group['name'])
'''
