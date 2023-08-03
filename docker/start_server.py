import subprocess

SERVER_PORT = 9001
SERVER_HOST = "0.0.0.0"

# Check if python is avaliable, using python3 if not.
result_code = subprocess.call("python", shell=True)
PYTHON_COMMAND = "python3" if result_code != 0 else "python"

CMD_MAKE_MIGRATIONS: str = f"{PYTHON_COMMAND} manage.py makemigrations"
CMD_MIGRATE: str = f"{PYTHON_COMMAND} manage.py migrate"
CMD_RUNSERVER: str = f"{PYTHON_COMMAND} manage.py runserver {SERVER_HOST}:{SERVER_PORT}"



subprocess.call(CMD_MIGRATE, shell=True)
subprocess.call(CMD_MAKE_MIGRATIONS, shell=True)
subprocess.call(CMD_RUNSERVER, shell=True)