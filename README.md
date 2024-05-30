# phyton-startkit

A simple Python Library to learn about this technology

# Before Starting

1. Install GIT [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

2. Install Python [here](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/cli/pip_install/)

3. Learn the basics about Git [here](https://docs.github.com/en/get-started/using-git/about-git)

# Setup

1. Clone this repository

2. Open the terminal and navigate to the folder where you cloned it

3. Create a new file called `.env` and add the following information:

```bash
  SERVER_VERSION=1.0.00
  SERVER_PORT=4005
  SERVER_LOG_LEVEL=info
```

4. Install the packages & Run the app

```bash
  cd python-startkit
  pip install requirements.txt
  cd src
  python main.py
```

# Test the execution

The correct execution of this package should enable you to run the following URL in your webbrowser:

http://localhost:4005/api/hello-world

# Expected Load Messages

```bash
INFO:     Will watch for changes in these directories: ['/...path.../phyton-startkit/src']
INFO:     Uvicorn running on http://0.0.0.0:4005 (Press CTRL+C to quit)
INFO:     Started reloader process [77670] using WatchFiles
INFO:     Started server process [77672]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

and once you load `http://localhost:4005/api/hello-world`: 

```bash
# this should be added...

INFO:     127.0.0.1:56087 - "GET /api/hello-world HTTP/1.1" 200 OK
```
