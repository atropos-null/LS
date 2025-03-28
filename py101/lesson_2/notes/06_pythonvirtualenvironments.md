## Python Virtual Enviroment

[Reference Page](https://launchschool.com/lessons/a29e9831/assignments/29e1c477)

By using virtual environments, you can:

* Manage project-specific dependencies without affecting the global Python environment.
* Avoid conflicts between different projects that require different library versions.
* Keep your development environment clean and portable.
* Ensure consistent development environments across different machines.
* Use the newest versions of Python (3.12 and up).

#### Setting up virtual enviroments:

**Step 1**: mentally decide on a centralized location for your virtual environments. 
We recommend using the conventional `~/.venv directory`.

**Step 2**: create the ~/.venv directory:
`mkdir ~/.venv`

_You can disregard any errors that say that .venv already exists. That just means you've 
already created it._

#### Setting Up Virtual Environments on GitHub Codespaces:

###### Set up a .local directory

```
mkdir -p ~/.local
cd ~/.local
```

* Download and install Python 3.9.20. Don't worry about what the various commands do.
```
wget https://www.python.org/ftp/python/3.9.20/Python-3.9.20.tgz
tar -xf Python-3.9.20.tgz
cd Python-3.9.20
./configure --prefix=$HOME/.local/opt/python-3.9.20
make -j 8
make install
cd ..
rm -fr Python-3.9.20*
```

###### Download and install Python 3.11.10. Don't worry about what the various commands do.

```
wget https://www.python.org/ftp/python/3.11.10/Python-3.11.10.tgz
tar -xf Python-3.11.10.tgz
cd Python-3.11.10
./configure --prefix=$HOME/.local/opt/python-3.11.10
make -j 8
make install
cd ..
rm -fr Python-3.11.10*
```

####### Return to your normal codespaces directory
cd /workspaces/codespaces-blank/

###### Set up a virtual environment for Python 3.9.20 in ~/.venv/env_a
```
~/.local/opt/python-3.9.20/bin/python3 -m venv ~/.venv/env_a
source ~/.venv/env_a/bin/activate
python --version            # Should show version 3.9.20
```

####### Set up a virtual environment for Python 3.11.10 in ~/.venv/env_b
####### We also need to install Flask 2.3.1

```
~/.local/opt/python-3.11.10/bin/python3 -m venv ~/.venv/env_b
source ~/.venv/env_b/bin/activate
python --version            # Should show version 3.11.10
pip3 install flask==2.3.1
```

####### Set up another virtual environment for Python 3.11.10 in ~/.venv/env_c
####### We also need to install Flask 2.1.2, which requires Werkzeug 2.2.2

```
~/.local/opt/python-3.11.10/bin/python3 -m venv ~/.venv/env_c
source ~/.venv/env_c/bin/activate
python --version            # Should show version 3.11.10
pip3 install werkzeug==2.2.2 flask==2.1.2
```

####### Deactivate the ~/.venv/env_c virtual environment
```
deactivate
```

####Using Virtual Environments

Once your virtual environment is set up and your application is ready to run:

1) Activate the desired virtual environment (if it isn't already activated).
2) Run the application
3) Deactivate the virtual environment (or activate another virtual environment).

```
source ~/.venv/env_a/bin/activate           # Step 1
python a.py                                 # Step 2
deactivate                                  # Step 3

source ~/.venv/env_b/bin/activate           # Step 1
python b.py                                 # Step 2
deactivate                                  # Step 3

source ~/.venv/env_c/bin/activate           # Step 1
python c.py                                 # Step 2
deactivate                                  # Step 3
```

**Note to ME**: It's not on a PATH right now.

when I want to install something in one of these two:
``` /home/vscode/.local/opt/python-3.9.20/bin/pip3 install some-package ```
