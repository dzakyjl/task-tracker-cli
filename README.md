# Task Tracker

This is my solution for project [task-tracker](https://roadmap.sh/projects/task-tracker) from [roadmap.sh](https://roadmap.sh/)

## How to use

Run the following command after cloning the repository:

```
git clone https://github.com/dzakyjl/task-tracker-cli.git
cd task-tracker-cli
```

Run the following command to build and run the project:

```
# Adding tasks
python task-cli.py add "Cook dinner"

# Updating tasks
python task-cli.py update 1 "Buy groceries and cook dinner"

# Deleting tasks
python task-cli.py delete 1

# Marking tasks
python task-cli.py mark todo 1
python task-cli.py mark in-progress 1
python task-cli.py mark done 1

# Listing tasks
python task-cli.py list
python task-cli.py list done
python task-cli.py list in-progress
```
