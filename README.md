# GitHub Repo Automation Tool

This command line tool automates the process of initializing a local Git repository, creating a remote GitHub repository via the GitHub API, optionally adding a `.gitignore` file, staging changes, committing, and performing the initial push to the remote repository.

## Operating Systems
MacOS

## Features

- Initialize a local Git repository.
- Create a remote repository on GitHub.
- Optionally add a `.gitignore` file.
- Stage changes.
- Commit changes.
- Push the initial commit to the remote repository.

## Requirements

- Python >=3.10
- Git
- GitHub account and authorization token

## Installation
```bash
pip install create-remote-repo
```

## Usage
```bash
create-remote-repo -rn <repo-name> -gu <github-username> -t <github-token> -d <working-directory> [-i <include-gitignore>] [-p <private>]
```

## Example
```bash
create-remote-repo -rn my-new-repo -gu myusername -t mytoken -d /path/to/working/directory -i y -p y
```

This command will:

1. Initialize a Git repository in the specified local working directory.
2. Create a remote repository named my-new-repo under the GitHub account myusername.
3. Add a .gitignore file to the repository.
4. Stage all changes.
5. Commit the changes.
6. Push the initial commit to the private remote repository.

## Set up Environment Variables
To avoid manually entering your GitHub username and token each time, you can set up environment variables.

Follow these steps to permanently set up environment variables in MacOS:

### Open You Shell Configuration File
```bash
nano ~/.zshrc
```
**Note**: Depending on your shell (like Bash or Zsh), edit the appropriate configuration file. For Bash, it's usually `~/.bash_profile` or `~/.bashrc`. For Zsh, it's `~/.zshrc`.

### Add Environment Variables
Add the following lines to the configuration file, replacing YOUR_GITHUB_USERNAME and YOUR_GITHUB_TOKEN with your GitHub credentials:
```bash
export GITHUB_USERNAME="YOUR_GITHUB_USERNAME"
export GITHUB_TOKEN="YOUR_GITHUB_TOKEN"
```

### Reload the Config File to Apply Changes
```bash
source ~/.bash_profile   # For Bash
source ~/.zshrc          # For Zsh
```

### Verify Environment Variables
```bash
echo $GITHUB_USERNAME
echo $GITHUB_TOKEN
```


## CLI Arguments

| Argument                     | Description                                                                                      | Required | Default Value            |
|------------------------------|--------------------------------------------------------------------------------------------------|----------|--------------------------|
| `-rn`, `--repo-name`         | The name of the remote repository you want to create.                                            | Yes      | None                     |
| `-gu`, `--github-username`   | The username of your GitHub account.                                                             | No       | `global_github_username` |
| `-t`, `--github-token`       | Your GitHub authorization token.                                                                 | No       | `global_github_token`    |
| `-d`, `--working-directory`  | The absolute path to the local working directory where the repository should be initialized.     | Yes      | None                     |
| `-i`, `--include-gitignore`  | Enter `y` if you want to add a `.gitignore` file to your repository, otherwise enter `n`.        | No       | `n`                      |
| `-p`, `--private`            | Enter `y` if you want to make the remote repository private, otherwise enter `n`.                | No       | `n`                      |

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/Kimmm-c/automate-create-remote-repo/blob/9c1d5213b39def985fc7cbfb1c4f15a2e7b74b57/LICENSE) file for details.

## Acknowledgements
Created and maintained by Kim Chung.
