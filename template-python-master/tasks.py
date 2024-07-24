from robocorp.tasks import task

@task
def minimal_task(number, alo):
    message = "Hello"
    message = message + " World!"
    message = message + str(number)
    message = message + alo
