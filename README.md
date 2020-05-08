# HERCULES - HRM/PAYROLL Suite
A web application to address the management needs of a company built with flask,python and sqlite.

Features:<br />
* Add/Update employee's profile<br />
* Salary calculation by uploading attendance sheet as CSV<br />
* Inbuilt email feature to send salary slips to respective employees through their registered email IDs<br />
* Make sure python3 and flask are installed.

### Clone the repository

In Windows : 
* Open command prompt inside project directory
```shell
>set FLASK_APP=main.py
>set FLASK_ENV=development
>set FLASK_RUN_PORT=5000
>flask run
```
In Linux/macOS :
* Open terminal inside project directory

```bash
$ export FLASK_APP=main.py
$ export FLASK_ENV=development
$ export FLASK_RUN_PORT=5000
$ flask run
```
* Open browser and go to localhost:5000.
