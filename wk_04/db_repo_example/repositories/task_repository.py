from db.run_sql import run_sql
from models.task import Task
import repositories.user_repository as user_repository


def select_all():
    tasks = []
    sql = "SELECT * FROM tasks"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select( row['user_id'] )
        # create a new task object
        new_task = Task(
            row['description'], 
            user, 
            row['duration'], 
            row['completed'],
            row['id']
        ) 
        # append to the list 
        tasks.append(new_task)

    return tasks


# delete_all

def delete_all():
    sql = "DELETE FROM tasks"
    run_sql(sql) 

# delete(id)

def delete(id):
    sql = "DELETE FROM tasks WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# save(task) 

def save(task):
    sql = """
    INSERT INTO tasks
        (description, user_id, duration, completed)
        VALUES (%s, %s, %s, %s)
        RETURNING *
    """
    values = [task.description, task.user.id, task.duration, task.completed]

    results = run_sql(sql, values)
    id = results[0]['id']
    task.id = id

    return task
# select(id0)

def select(id):
    task = None
    sql = "SELECT * FROM tasks where id = %s"
    values = [id]
    results = run_sql(sql, values)

    if len(results) > 0:
        selected_task = results[0]
        user = user_repository.select(selected_task['user_id'])
        task = Task(
            selected_task['description'],
            user,
            selected_task['duration'],
            selected_task['completed'],
            selected_task['id']
        )
    
    return task

# update(task)
def update(task):
    sql = """
        UPDATE tasks 
            SET (description, user_id, duration, completed) 
                = (%s, %s, %s, %s) 
            WHERE id = %s
    """
    values = [
        task.description, task.user.id, task.duration, task.completed,
        task.id
    ]

    run_sql(sql, values)

def tasks_for_user(user):
    sql = """
        SELECT * FROM tasks 
        WHERE user_id = %s
    """

    values = [user.id]

    results = run_sql(sql, values)

    user_tasks = []
    for row in results:
        task = Task(
            row['description'], 
            user,
            row['duration'],
            row['completed'],
            row['id']
        )
        user_tasks.append(task)
    return user_tasks