import os
import requests
from autofunccli import cmdfunc


def curlInput(year, day, dayPath):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    # get cookie session from session.txt
    try:
        with open(f"{os.getcwd()}/session.txt", "r") as f:
            session = f.read()
            cookies = {"session": session}

            r = requests.get(url, cookies=cookies)
            input = r.text
            f = open(dayPath + "/input.txt", "a")
            f.write(input)
            f.close()
            solution_f = open(dayPath + "/solution.py", "w")
            with open("template.py") as f:
                lines = f.readlines()
                solution_f.writelines(lines)
    except FileNotFoundError:
        print("File session.txt missing at root's project")
        os.unlink(dayPath)
        return


@cmdfunc
def prepareOneDay(day: str, year: str = "2020"):
    # detect the current working directory and print it
    currentDir = os.getcwd()
    dayPath = f"{currentDir}/{year}/day_{day}"
    if not os.path.exists(dayPath):
        try:
            os.mkdir(dayPath)
            curlInput(year, day, dayPath)
        except OSError:
            print("Creation of the directory %s failed" % dayPath)
    else:
        print(f"Directory for {day}/{year} already exists")


prepareOneDay.main(__name__)
