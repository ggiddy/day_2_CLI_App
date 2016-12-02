
"""CLI app implemented in docopt, httplib 

Usage:
    app.py all
    app.py fetch <post_id>
    app.py edit <title> <body>
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

if __name__ == '__main__':
    ARGS = docopt(__doc__, version='1.0')

if ARGS['all']:
    print 'all called'
if ARGS['fetch']:
    print 'add called'
if ARGS['edit']:
    print 'add called'
if ARGS['delete']:
    print 'add called'
