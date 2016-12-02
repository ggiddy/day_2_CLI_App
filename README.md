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

 To run the application, navigate to the app/ directory:
 ```
 $ cd app/

 ```
 
 **Commands**
 
 ```
 python app.py new <title> <body>
 python app.py all
 python app.py fetch <post_id>
 python app.py edit <post_id> <title> <body>
 python app.py delete <post_id>
 python app.py (-h | --help)

```
 
