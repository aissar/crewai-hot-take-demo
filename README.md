# Installation

First, if you haven't already, setup the python environment.

```bash
brew install pyenv
env PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install 3.12.7
pyenv init
pyenv shell 3.12.7
```

Next, if you haven't already, install crewai

```bash
pip install 'crewai[tools]'
```

# Create a new crewai project

To create a new crew project, run this from the root folder of your git repo:

```bash
crewai create crew <project_name>
```

# Set environment variables

Add your `OPENAI_API_KEY` and other keys (if applicable) into the `.env` file before running the crew.

See sample below:

```
MODEL=gpt-4o-mini
OPENAI_API_KEY=<insert-key-here>
SERPER_API_KEY=<insert-key-here>
```

# Run an existing crewai project

Navigate to the crewai project directory and run this:

```bash
cd <project_name>
pyenv shell 3.12.7
crewai run
```

# Customising the crew

- Modify `<project_name>/src/<crew_name>/config/agents.yaml` to define your agents
- Modify `<project_name>/src/<crew_name>/config/tasks.yaml` to define your tasks
- Modify `<project_name>/src/<crew_name>/tools` to add custom tools
- Modify `<project_name>/src/<crew_name>/crew.py` to add your own logic, tools and specific args
- Modify `<project_name>/src/<crew_name>/main.py` to add custom inputs for your agents and tasks

# Helpful links

- Official quickstart guide: https://docs.crewai.com/quickstart
- Example projects: https://docs.crewai.com/examples/example
- Community support: https://community.crewai.com/
