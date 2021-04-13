import redis

redis_host = "localhost"
redis_port = 6379
redis_password = ""
r = redis.StrictRedis(host=redis_host, port=redis_port,password=redis_password, decode_responses=True)

db = " "
def print_header():
    header_text = ''
    TEXT = ' Todo List  \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_todo():
    todo = input('Enter todo: ')
    return todo


def store_todo(task):
    if task:
          r.sadd(db, task)
        

def get_all_todo():
    return r.smembers(db)


def show_all_todos(todos):
    print('All Todos: ')
    for todo in todos:
        print(todo)

def delete_todo(todo):
    if todo and r.exists(db):
        r.srem(db, todo)

if __name__ == '__main__':
    print_header()
    todo = get_todo()
    while todo:
        store_todo(todo)
        todo = get_todo()

    print()
    todos = get_all_todo()
    show_all_todos(todos)

    print('\nDelete todo')
    todo = get_todo()
    while todo:
        delete_todo(todo)
        todo = get_todo()

    print()
    todos = get_all_todo()
    show_all_todos(todos)

