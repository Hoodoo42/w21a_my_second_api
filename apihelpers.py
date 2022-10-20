import mariadb
import dbcreds
import json
import dbhelpers as dbh

def make_api(statement):
    results = dbh.run_statement(statement)
    if (type(results) == list):
        animal_json = json.dumps(results, default=str)
        return animal_json
    else:
        return "Sorry there is an error"

# takes in the client data sent and the expected data stored in the database procedure.
# loops through each data piece in the expected data and if the sent data matches the  stored data it will send back a success
# if data does does not match it will return as undefined and return a message of the specific missing data that is required
def check_endpoint_info(sent_data, expected_data):
    for data in expected_data:
        if(sent_data.get(data) == None):
            return f"The {data} argument is required!"