class Request:
    def __init__(self,
                 repo_name=None,
                 github_username=None,
                 github_token=None,
                 working_directory=None,
                 include_gitignore=None):
        self.repo_name = repo_name
        self.github_username = github_username
        self.github_token = github_token
        self.working_directory = working_directory
        self.include_gitignore = True if include_gitignore.lower() == "y" else False

    def __str__(self):
        return f"""
        repo_name: {self.repo_name},
        github_username: {self.github_username}
        github_token: {self.github_token}
        working_directory: {self.working_directory}"""
