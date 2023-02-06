# Pre-Reqs
1. Python 3.10.9
2. pip 22.3.1
3. Install dependencies
```
$ pip install -r requirements.txt
```

# Instructions
1. Create a virtualenv with the desired python interpreter:
```
$ virtualenv -p python3.10 cron_parser
```
2. To activate the virtual environment run the following command:
```
$ . ./cron_parser/bin/activate
```
3. To deactivate the virtualenv 
```
$ deactivate
```
4. To upgrade pip:
```
$ pip install --upgrade pip
```
5. To run the command:
```
$ python main.py "*/15 0 1,15 * 1-5 /usr/bin/find"
```
NOTE: The cron expression must be inside quotes ("")
