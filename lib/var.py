import json

def var(line, variables):
    variable = line.split("var ")[1]
    variable_name = variable.split(" ")[0]
    variable_data = variable.split(f"{variable_name} ")[1]

            
    variables[variable_name] = variable_data
    json.dumps(variables)

def varB(line, variables):
    variable = line.split("var ")[1]
    variable_name = variable.split(" ")[0]
    variable_data = variable.split(f"{variable_name} ")[1]
    variables[variable_name] = variable_data
    json.dumps(variables)
    py_file = f"{variable_name} = {variable_data}\n" 
    return py_file   