
"""CLI app implemented in docopt, httplib 

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

API_URL = 'https://jsonplaceholder.typicode.com/posts/'

if __name__ == '__main__':
    ARGS = docopt(__doc__, version='1.0')

if ARGS['new']:
    # POST
    payload = {
        'title': ARGS['<title>'],
        'body': ARGS['<body>']
    }
    res = requests.post(API_URL, data = payload)

    if res.status_code == 200:
        print "Successfully created a new post"
    else:
        print "Problem creating post. Please check if you have write access"

if ARGS['all']:
    # GET
    res = requests.get(API_URL)
    if res.status_code == 200:
        json_res = res.json()
        print json_res
    else:
        print 'There was a problem processing your request'

if ARGS['fetch']:
    # GET specific
    post_id = ARGS['<post_id>']
    res = requests.get(API_URL + post_id)

    if res.status_code == 200:
        print "Successful"
        json_res = res.json()
        print json_res
    else:
        print 'There was a problem accessing your post'

if ARGS['edit']:
    # PUT 
    payload = {
        'title': ARGS['<title>'],
        'body': ARGS['<body>']
    }
    res = requests.put(API_URL+ARGS['<post_id>'], data = payload)

    if res.status_code == 200:
        print 'Edit successful'
        json_res = res.json()
        print json_res
    else:
        print 'Problem editting post'

if ARGS['delete']:
    # DELETE
    res = requests.delete(API_URL+ARGS['<post_id>'])

    if res.status_code == 200:
        print 'Post successfully deleted'
    else:
        print 'Problem encountered deleting post'
