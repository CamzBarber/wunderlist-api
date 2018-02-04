"""
Wunderlist API

Cameron Barber - Feb 2018
"""

import requests
import json

access_token = 'xxx'
client_id = 'xxx'
list_id = 123456789

headers = {'X-Access-Token': access_token, 'X-Client-ID': client_id, 'Content-Type': 'application/json'}


def error_handle(code):
    if code.status_code in (400, 401, 404):
        raise ValueError('Wunderlist error', code)


def get_tasks(completed):
    params = {'completed': completed, 'list_id': list_id}
    r = requests.get('https://a.wunderlist.com/api/v1/tasks', headers=headers, params=params)
    j = json.loads(r.text)
    ids = []
    revisions = []

    for i in j:
        # print(i['title'])  # Prints each task name.
        revisions.append(i['revision'])
        ids.append(i['id'])

    error_handle(r)
    return ids, revisions


def post_task(title, date, starred):
    to_json = json.dumps({'list_id': list_id, 'title': title, 'due_date': date, 'starred': starred})
    r = requests.post('https://a.wunderlist.com/api/v1/tasks', headers=headers, data=to_json)
    error_handle(r)


def delete_task(task_id, revise):
    r = requests.delete('https://a.wunderlist.com/api/v1/tasks/'+task_id, headers=headers, params={'revision': revise})
    error_handle(r)


def delete_all(completed):
    all_tasks = get_tasks(completed)
    for idx, x in enumerate(all_tasks[0]):
        delete_task(str(x), all_tasks[1][idx])


"""
------------
EXAMPLE USES:
------------
"""


"""
GET TASKS: returns a list of ids and revisions (option to print title)
    - Arguments:
        - completed (boolean): True to show completed, False to show active
"""
# get_tasks(False)


"""
POST TASK: creates a given task
    - Arguments:
        - title (string): the title of the task to be created
        - date (string): (OPTIONAL*) ISO8601 date to set the task for, e.g. 2018-02-05
        - starred (boolean): (OPTIONAL*) True to be starred, False to not
"""
# post_task('Test Task', '', False)


"""
DELETE TASK: deletes a given task
    - Arguments:
        - task_id (string): the id to be deleted 
        - revise (integer): the id revision number, see Wunderlist API documents on this
"""
# delete_task('0123456789', 1)


"""
DELETE ALL TASKS: deletes all tasks
    - Arguments:
        -completed (boolean): True deletes completed tasks, False deletes active tasks
"""
# delete_all(False)


# (OPTIONAL*): these fields can be left empty or filled with the default value if not needed
