#!/usr/bin/python3
""" Todo list progress for employee """

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    req_f = f'https://jsonplaceholder.typicode.com/users/{id}'
    emp_req = requests.get(req_f)
    if emp_req.status_code == 200:
        resp_emp = emp_req.json()
        name = resp_emp.get('name')
        req_f = f'https://jsonplaceholder.typicode.com/todos?userId={id}'
        todos_req = requests.get(req_f)
        if todos_req.status_code == 200:
            resp_todos = todos_req.json()
            completed_list = [todo for todo in resp_todos if todo.get('completed')]
            completed_t_c = len(completed_list)
            all_c = len(resp_todos)
            print(f'Employee {name} is done with tasks({completed_t_c}/{all_c}):')
            for todo in completed_list:
                print(f'\t {todo.get("title")}')
    else:
        print(f"Employee with ID {id} not found.")
