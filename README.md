## A Chess Game API made with Django



For Documentation and reference to the Game design, see docs [here](https://wawanjohi.github.io/chess-python/)

## This project uses [pre-commit](https://pre-commit.com/) and [black](https://pypi.org/project/black/) for formatting.
### Quick Start
- [Clone Repo](#clone-the-repo)
- [Setup Virtual Env](#setup-virtual-env)
- [Setup Channels](#setup-channels)
- [Setup Database and Firebase](#setup-database-and-firebase)
- [Setup Superuser](#setup-superuser)
- [Running the project](#run-the-project)
- [Conclusion](#sign-up-as-an-organization-now-you-can-write-bugs)






## Clone the repo:
with https
```sh
git clone https://github.com/wawanjohi/chess-python.git
```
or SSH
```sh
git clone git@github.com:wawanjohi/chess-python.git
```
or with Git CLI
```sh
gh repo clone wawanjohi/chess-python
```


## Setup virtual env:
Linux or Mac:
```sh
virtualenv venv && source venv/bin/activate

```

Windows:
Create the environment `venv` and run this on powershell: <br>

```sh
.\venv\Scripts\Activate.ps1
```

While at it, copy `.env.example` to `.env` and prepopulate the values as you need to.

## Setup Channel Layers:

You can use in-memory channel layers, but be sure to move to a production-ready channel layer such as Redis.


### Setting up InMemoryChannelLayer:

Add this to your Setting

```py
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels.layers.InMemoryChannelLayer"
        }
    }
```

### Setup channel layers to use Redis


Make sure Redis is installed and working on your machine. This works out of the box on Mac or Linux.

Ubuntu/Debian
```sh
sudo apt install redis
```

Arch/Manjaro
```sh
sudo pacman -S redis
```

Fedora
```sh
sudo dnf -y install redis
```

Install with [Snap](https://snapcraft.io/) (Compatible with most linux Distros)
```sh
sudo snap install redis
```

For Windows, you will either have to use Docker or other third-party ways for connecting to a linux environment as Redis doesn't work out of the box.

[Docker](https://www.docker.com/)
```sh
docker run -it --name chess-python-redis -d redis
```

We'd highly recommend that you use [Memurai](https://www.memurai.com/) if you don't intend to use [Docker](https://www.docker.com/)


Add this to your settings:

```py
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [("127.0.0.1", 6379)],
            },
        },
    }
```


## Setup pre commit:
Adjust the python version on `.pre-commit-config.yaml` to match yours (3.9.x recommended) on this line: <br>
`language_version: python3.x.x`


## Run Project

Migrate and create superuser: <br>
```sh
python manage.py migrate
python manage.py createsuperuser

```

## Run the project:
```sh
python manage.py runserver
```

## Now you can write bugs :)
