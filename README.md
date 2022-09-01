# How to use this repo?

Before anything, you'll need to have `python` and a `Unix shell` installed on your computer.

- [Python](https://www.python.org/downloads/)
- The Mac OS Terminal is ready to go![^1]

1. Make a `python` virtual environment in your project

   ```SHELL
   $ cd project-path
   project-path $ python3 -m venv .env
   ```

2. Activate it

   ```SHELL
   project-path $ source .env/bin/activate
   ```

3. Now you can use it, but before checking which `python` and `pip` (package manager) you're using

   ```SHELL
   (.env) project-path $ which python
   # project-path/scripts/.env/bin/python -> This is good because is in your project

   (.env) project-path $ which python
   # project-path/scripts/.env/bin/pip -> Also good! you're free to go
   ```

   - If there's a problem with your install like `python not found` you could try deleting the `.env` folder and running the `python3 -m venv .env` command again

4. Install the dependencies of the repository in your environment

   - Individually
     ```SHELL
     (.env) project-path $ pip install brotli
     (.env) project-path $ pip install font tools
     ```
   - Or with the `requirements.txt` file
     ```SHELL
     (.env) pip install -r requirements.txt
     ```

Now you can start playing with the scripts we have for you!
Go to the [scripts](./scripts) folder to check what we have to improve your workflow.

> If you want a custom script or you have a complex font engineering project feel free to contact us at [anchor@letterengine.com](mailto:anchor@letterengine.com)

[^1]: Windows users will need to install it and there are also alternatives with more functionality for Mac OS users.
