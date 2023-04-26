from cookiecutter.main import cookiecutter

def create_monitoring():
    cookiecutter("./templates", output_dir="./dags")