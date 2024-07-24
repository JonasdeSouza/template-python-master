from robocorp.tasks import task
from robocorp.workitems import WorkItems

@task
def main():
    workitems = WorkItems()
    input_item = workitems.get_input_work_item()
    payload = input_item.payload
    
    # Assuming the payload is a dictionary that contains the arguments you need
    arg1 = payload.get("number")
    arg2 = payload.get("alo")
    minimal_task(arg1, arg2)

    
def minimal_task(number, alo):
    message = "Hello"
    message = message + " World!"
    message = message + str(number)
    message = message + alo
