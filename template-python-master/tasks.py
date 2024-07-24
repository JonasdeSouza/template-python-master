from robocorp.tasks import task

@task
def minimal_task(number):
    message = "Hello"
    message = message + " World!"
    message = message + str(number)
