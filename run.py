import os
from autofunccli import cmdfunc


@cmdfunc
def run_solution(day: str, year: str = "2020"):
    current_dir = os.getcwd()
    day_path = f"{current_dir}/{year}/day_{day}/solution.py"

    os.system(
        "PYTHONDONTWRITEBYTECODE=1 python3.9 -m pytest -p no:cacheprovider " + day_path)
    os.system("python3.9 " + day_path)


run_solution.main(__name__)
