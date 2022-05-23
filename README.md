# Dukka Backend Engineer Test

## Task: Create a transaction receipt generating backend for with access control


#### _A quick and dirty solution to the test_

Test challenge completed and hosted on heroku at:
[dukka-test.herokuapp.com](dukka-test.herokuapp.com)

Primary API routes start at [dukka-test.herokuapp.com/user](dukka-test.herokuapp.com/user) and documentation is provided at the index page

Test the API endpoints using an API client such as Postman or RapidAPI

Unauthorised access to generated receipts is not provided. All receipts are stored at the root
directory in the `src/` folder

Authorised receipt download at endpoint [dukka-test.herokuapp.com/user/receipt/download](dukka-test.herokuapp.com/user/receipt/download)

**Note**: The database is cleared everytime the dyno sleeps. All activites will need to be repeated
