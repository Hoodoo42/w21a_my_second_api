from cProfile import run
from unittest import result
import mariadb
from flask import Flask, request, make_response
import json
from apihelpers import check_endpoint_info
import dbhelpers as dbh

app = Flask(__name__)
# ITEM

@app.get('/api/item')
def get_items():
    #store the results of the procedure call in results
    results = dbh.run_statement('CALL get_items()')
# if the type of the results is a list, meaning it has returned something, then respond with a success/ else return an error. 500 being a server error
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps('sorry error', default=str), 500)        
    

@app.post('/api/item')
def add_item():
    # if api needs an argument then you must check that the client data sent matches the expected data. 
    # is_valid is storing the reults of this check. the check is returning an error if no match. so if is_valid is != none that means it has retuned an error
    is_valid = check_endpoint_info(request.json, ['name', 'description', 'quantity'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)
# to insert the argument us as many ? as there are arguments. then request.json.get() for each argument name
    results = dbh.run_statement('CALL new_item(?,?,?)', [request.json.get('name'), request.json.get('description'), request.json.get('quantity')])
    if(type(results) == list):
        return make_response(json.dumps(results), 200)
    else:
        return make_response(json.dumps('sorry error'), 500)            

@app.patch('/api/item')
def update_item():
    is_valid = check_endpoint_info(request.json, ['id', 'quantity'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = dbh.run_statement('CALL add_stock(?,?)', [request.json.get('id'), request.json.get('quantity')])
    if(type(results) == list):
        return make_response(json.dumps(results), 200)
    else:
        return make_response(json.dumps('sorry error'), 500)  

@app.delete('/api/item')
def delete_item():
    is_valid = check_endpoint_info(request.json, ['id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = dbh.run_statement('CALL delete_item(?)', [request.json.get('id')])

    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps('Sorry error', default=str), 500)    


# EMPLOYEE

@app.get('/api/employee')
def get_employee():
    is_valid = check_endpoint_info(request.args, ['id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = dbh.run_statement('CALL get_employee(?)', [request.args.get('id')]) 
    if(type(results) == list):
       return make_response(json.dumps(results, default=str), 200)
    else:
       return make_response(json.dumps('sorry error', default=str), 500)      

@app.post('/api/employee')
def new_employee():
    is_valid = check_endpoint_info(request.json, ['name', 'position', 'hourly_wage'])
    if(is_valid != None):
            return make_response(json.dumps(is_valid, default=str), 400)

    results = dbh.run_statement('CALL new_employee(?,?,?)', [request.json.get('name'), request.json.get('position'), request.json.get('hourly_wage')]) 
    if(type(results) == list):
           return make_response(json.dumps(results, default=str), 200)
    else:
           return make_response(json.dumps('sorry error', default=str), 500)

@app.patch('/api/employee')
def wage_adjust():
    is_valid = check_endpoint_info(request.json, ['id', 'hourly_wage'])
    if(is_valid != None):
            return make_response(json.dumps(is_valid, default=str), 400)

    results = dbh.run_statement('CALL wage_adjust(?,?)', [request.json.get('id'), request.json.get('hourly_wage')]) 
    if(type(results) == list):
           return make_response(json.dumps(results, default=str), 200)
    else:
           return make_response(json.dumps('sorry error', default=str), 500)


# this one does delete the employee however has "Programming Error Cursor doesn't have a result set"
@app.delete('/api/employee')
def fire_employee():
    is_valid = check_endpoint_info(request.json, ['id'])
    if(is_valid != None):
            return make_response(json.dumps(is_valid, default=str), 400)

    results = dbh.run_statement('CALL youre_fired(?)', [request.json.get('id')]) 
    if(type(results) == list):
           return make_response(json.dumps(results, default=str), 200)
    else:
           return make_response(json.dumps('sorry error', default=str), 500)

app.run(debug=True)