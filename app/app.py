#! .env/bin/python
"""CLI app implemented in docopt, and requests library

Usage:
    app.py new <title> <body>
    app.py all
    app.py fetch <post_id>
    app.py edit <post_id> <title> <body>
    app.py delete <post_id>
    app.py (-h | --help)

Arguments
    <command>
    <post_id>  The post id
    <title> The post title
    <body>  The post body

Options:
   -h --help    Show this screen
"""
from docopt import docopt
import requests
from termcolor import colored

API_URL = 'https://jsonplaceholder.typicode.com/posts/'

if __name__ == '__main__':
    ARGS = docopt(__doc__, version='1.0')

if ARGS['new']:
    # POST
    PAYLOAD = {
        'title': ARGS['<title>'],
        'body': ARGS['<body>']
    }

    RES = requests.post(API_URL, data=PAYLOAD)

    if RES.status_code == 201:
        print colored('Successfully Created', 'green')
        for post in RES:
            print post
    else:
        print colored('Error: Problem creating post. ' \
            'Please check if you have write access', 'red')

if ARGS['all']:
    # GET
    RES = requests.get(API_URL)
    if RES.status_code == 200:
        print colored('Getting all posts...', 'green')
        for post in RES:
            print post
    else:
        print colored('Error: There was a problem ' \
            'processing your request', 'red')

if ARGS['fetch']:
    # GET specific
    POST_ID = ARGS['<post_id>']
    RES = requests.get(API_URL + POST_ID)

    if RES.status_code == 200:
        print colored('Fetching post ' + POST_ID + ' successful', 'green')

        for post in RES:
            print post
    else:
        print colored('Error: There was a problem getting your post', 'red')

if ARGS['edit']:
    # PUT
    PAYLOAD = {
        'title': ARGS['<title>'],
        'body': ARGS['<body>']
    }
    RES = requests.put(API_URL+ARGS['<post_id>'], data=PAYLOAD)

    if RES.status_code == 200:
        print colored('Edit successful', 'green')
        for post in RES:
            print post
    else:
        print colored('Error: Problem editting post', 'red')

if ARGS['delete']:
    # DELETE
    POST_ID = ARGS['<post_id>']
    RES = requests.delete(API_URL+POST_ID)

    if RES.status_code == 200:
        print colored('Post ' + POST_ID + ' successfully deleted', 'green')
    else:
        print colored('Error: Problem deleting post', 'red')
