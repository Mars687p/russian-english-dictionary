# Run guide #

1. git clone https://github.com/Mars687p/russian-english-dictionary  
1. cd russian-english-dictionary  
1. pythom -m venv env && source env/bin/activate  
1. cp example.env .env  
1. Insert your telegram token to .env file  
1. source .env  
1. pip install -r requirements/development.txt  
1. touch db.sqlite  
1. python server.py   