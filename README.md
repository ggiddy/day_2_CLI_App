# Python CLI App
A simple CLI application that consumes a public API using a HTTP client library.

**Installation**

`$ git clone https://github.com/giddygitau/day_2_CLI_App.git`

`$ cd day_2_CLI_App`
 
 Create and activate a virtual environment.
 
 ```
 $ virtualenv .env
 $ source .env/bin/activate
 ```
 
 Install dependencies
 
 `$ pip install -r requirements.txt`
 
 **Commands**
 
 ```
 app.py new <title> <body>
 app.py all
 app.py fetch <post_id>
 app.py edit <post_id> <title> <body>
 app.py delete <post_id>
 app.py (-h | --help)

```
 
