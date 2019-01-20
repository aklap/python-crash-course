import requests

from operator import itemgetter

# Make API call, store response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status code:', r.status_code)

# Process info about each submission
submission_ids = r.json()
submission_dicts = []

# Get first 30 submission ids
for submission_id in submission_ids[:30]:
    # Make separate API call for each submission
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    # Make HTTP get request for that resource
    submission_r = requests.get(url)
    # Print the status of the above request
    print(submission_r.status_code)
    # Store the response in a variable as json
    response_dict = submission_r.json()

    # Store information as a dictionary for that specific submission_id
    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0),  # return the value for the given key otherwise return 0
    }

    # Add that dictionary to another dictionary that collects ALL posts
    submission_dicts.append(submission_dict)

    # Sort the order of the key-value pairs in the dictionary by number of comments
    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Loop through all of the posts we received in response and print them
for submission_dict in submission_dicts:
        print("\nTitle:", submission_dict['title'])
        print("Discussion Link:", submission_dict['link'])
        print("Comments:", submission_dict['comments'])
