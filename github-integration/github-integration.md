# Github integration wih python to create a PR Creators Tracker

wirting a small Python script that uses the GitHub API to fetch active pull requests from the Kubernetes repo and shows which users created them along with the count of PRs per user.

## How it works
-> Uses the [GitHub API](https://docs.github.com/en/rest) to get pull requests from `kubernetes/kubernetes`.
-> Converts the JSON response into a dictonary and extracts the `user.login` field.
-> Keeps a count of how many PRs each user has opened.
-> Prints the results in the terminal in the form of dictonary.


## Requirements
1. Python
2. `requests` library

--> we can install requests library from terminal or commad line by running below :
pip install requests
