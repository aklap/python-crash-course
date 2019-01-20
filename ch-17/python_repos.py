import requests


def get_repos(language):
    """Get repos using a specific language from GitHub."""
    # Make API call and store request
    language = language.lower()
    url = 'https://api.github.com/search/repositories?q=language:' + language + '&sort=stars'

    try:
        response = requests.get(url)  # Make HTTP 'get' request for the resource at URL
    except Exception as err:
        return 'Oops, something went wrong! Error: {}'.format(err)
    return response


def check_status(response_dict):
    """Return the status code of an HTTP request."""
    return 'Status: ' + str(response.status_code)  # Check if successful or not


def response_keys(response_dict):
    """Return the keys of the GitHub response."""
    # Store API response in variable
    return 'Keys: ' + (', ').join(sorted(response.keys()))


def total_repos(response_dict):
    """Return total number of repos that use this language."""
    # All repos matching query
    return 'Total repos found: ' + str(response['total_count'])


def check_repo_amount(response_dict):
    """Check that we get up to 30 repos in specified language and no more."""
    repo_dicts = response['items']
    return 'Repos returned by search: ' + str(len(repo_dicts))


def repo_keys(repo_dict):
    """Return all length of keys, list of keys for a repo as a tuple."""
    # Look at first repo returned
    return (len(repo_dict.keys()), [key for key in sorted(repo_dict.keys())])


def display_info(repo_dict):
    """Return dictionary containing basic info about a repo."""
    print('\nSelected information about repo:')
    print('Name:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])

def get_repo_info(language):
    response = get_repos(language)
    repos_dict = response.json()

    check_status(response)
    response_keys(repos_dict)
    total_repos(repos_dict)
    check_repo_amount(repos_dict)

    for repo_dict in repos_dict['items']:
        display_info(repo_dict)

get_repo_info('python')
