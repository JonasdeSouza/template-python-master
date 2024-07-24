from robocorp.tasks import task
from robocorp import workitems 

@task
def main():
    item = workitems.inputs.current
    payload = item.payload
    
    # Assuming the payload is a dictionary that contains the arguments you need
    arg1 = payload.get("number")
    arg2 = payload.get("alo")
    minimal_task(arg1, arg2)


def minimal_task(number, alo):
    message = "Hello"
    message = message + " World!"
    message = message + str(number)
    message = message + alo
