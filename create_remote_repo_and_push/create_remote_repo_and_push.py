from .models.request import Request
from .handlers.CreateRemoteRepoHandler import CreateRemoteRepoHandler
from .handlers.CreateGitignoreHandler import CreateGitignoreHandler
import argparse
import os

username = os.getenv('GITHUB_USERNAME')
token = os.getenv('GITHUB_TOKEN')


def validate_request(request):
    if request.repo_name is None:
        raise ValueError("Remote repository name is required")
    elif request.working_directory is None:
        raise ValueError("Local working directory to initialize the repo is required")


def setup_request_commandline() -> Request:
    parser = argparse.ArgumentParser()
    parser.add_argument("-rn", "--repo-name", help="The name of the remote repository you want to create")
    parser.add_argument("-gu", "--github-username", help="The username of your Github account", default=username)
    parser.add_argument("-t", "--github-token", help="Your Github authorization token", default=token)
    parser.add_argument("-d", "--working-directory", help="The local working directory where the repo should be "
                                                          "initialized")
    parser.add_argument("-i", "--include-gitignore", help="Enter y if you want to add .gitignore to your repo, "
                                                          "otherwise enter n", default="n")

    try:
        args = parser.parse_args()
        request = Request(repo_name=args.repo_name,
                          github_username=args.github_username,
                          github_token=args.github_token,
                          working_directory=args.working_directory,
                          include_gitignore=args.include_gitignore)
        validate_request(request)
        return request

    except Exception as e:
        print(f'Error: {e}')
        quit()


def main():
    request = setup_request_commandline()

    create_repo_handler = CreateRemoteRepoHandler()

    if request.include_gitignore:
        create_gitignore_handler = CreateGitignoreHandler()
        create_gitignore_handler.set_next_handler(create_repo_handler)
        create_gitignore_handler.process(request)
    else:
        create_repo_handler.process(request)


if __name__ == '__main__':
    main()
