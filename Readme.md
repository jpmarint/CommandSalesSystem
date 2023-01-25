# Juan Sales Service in Command Line

This code simulates a CRUD to have a database in a CSV file for the clients for a store.

The system stores in a csv file the Name, email, position and company from each client.

In order to run the code, this system runs in a virtual environement for python 3.11

Install packages using requirements.txt:

```
git clone
python3 -m venv env
source StoreEnv/bin/activate
pip3 install -r requirements.txt
```
Install Packages using setup.py:

```
git clone
python3 -m venv env
source StoreEnv/bin/activate
pip3 install -e .
```

Cause this is a command line program in order to run and the instructions are as follows:

To run:
```
cd .\MainApp\
#Write commands
```

## Commands
```
jp clients --help (To see all the commands)
jp clients create       (Creates a client)
jp clients delete [uid] (Deletes a client)
jp clients list         (Shows a table)
jp clients update [uid] (Update client's info)
```