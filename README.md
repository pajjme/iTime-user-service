[![Build Status](https://travis-ci.org/pajjme/iTime-user-service.svg?branch=master)](https://travis-ci.org/pajjme/iTime-user-service)
# iTime-user-service
User service for iTime.



#First time setup
##Dependencies
* Python 3
* pip3 
* postgres



Install the python packages that are used:
```pip3 install -r /path/to/requirements.txt```


Install postgres, create a database and a user.
For exampele a database named `test_db` and user `test`.

Restore the database schema from the backup in the schema folder.

Edit the file .env_example with the database credentials.

For example:
```
export ITIME_DB="test_db"
export ITIME_USER="test"
export ITIME_DB_PASSWORD="password"
```

Source this file or put these enviornment variables into `.profile` or equal.

Then you should run `python3 main.py`
And it should work ... probably!



