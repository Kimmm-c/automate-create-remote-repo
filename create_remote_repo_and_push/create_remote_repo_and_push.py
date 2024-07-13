from .helpers.run_command import run_command as rc
from .models.request import Request
import argparse
import os

username = os.getenv('GITHUB_USERNAME')
token = os.getenv('GITHUB_TOKEN')


def setup_request_commandline() -> Request:
    parser = argparse.ArgumentParser()
    parser.add_argument("-rn", "--repo-name", help="The name of the remote repository you want to create")
    parser.add_argument("-gu", "--github-username", help="The username of your Github account", default=username)
    parser.add_argument("-t", "--token", help="Your Github authorization token", default=token)

    try:
        args = parser.parse_args()
        print(args)
    except Exception as e:
        print(f'Error: {e}')
        quit()


def main():
    request = setup_request_commandline()


if __name__ == '__main__':
    main()
