# Contributing

## Development
### Prerequisites
These software are the prerequisites to be able to work on this repo
1. uv
2. pyright (optional but helpful)
3. git

### Setup
To start working on this repo, follow these steps:
```bash
git repo clone https://github.com/mitthrawnuruodo14/PythonGame.git
cd PythonGame
uv sync
```
after this you should be able to run the project through:
```bash
uv run python main.py
```

optionally, you can also activate the virtual enviroment and run python directly
```bash
source .venv/bin/activate
python main.py
```

### Contributions
#### Commit convention
In commits, please use the following convention:
for commits where you implement a feature, please prefix it with "feat: "
for commits where you only refactor some code and behaviour DOESN'T change, prefix it with "refactor: "
for commits where you fix a bug or such, prefix with "fix: "
for commits where you only change documentation, prefix with "docs: "

#### Adding to the project
The project will have 2 base branches and as many feature branches as you wish.

##### The "main" branch
The main branch should always have a stable state and should never have work in progress code inside it.

##### The "dev" branch
The dev branch also should be stable, but here you can push features that are part of a bigger feature, but there shouldnt be 
work in progress code present on this branch. If a feature has been fully implemented you can merge with the main branch

##### The "feature/*" branch
You can do whatever you want in these branches, you can commit work in progress code and it doesnt have to be stable and you should
work in these branches until you feel that you have enough to merge with the dev branch.
The feature/ is just a convention, for example if you want to implement a player or such then you can make a branch "feature/player"
and commit once you are done implementing the player
