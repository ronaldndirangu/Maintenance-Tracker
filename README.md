# Maintenance-Tracker
[![Build Status](https://travis-ci.org/ronaldndirangu/Maintenance-Tracker.svg?branch=develop)](https://travis-ci.org/ronaldndirangu/Maintenance-Tracker)
[![codecov](https://codecov.io/gh/ronaldndirangu/Maintenance-Tracker/branch/develop/graph/badge.svg)](https://codecov.io/gh/ronaldndirangu/Maintenance-Tracker)


## Introduction
An application that provides users with the ability to reach out to operations or repairs department regarding repair or maintenance requests and monitor the status of their request.
### Features
1. Users can create an account and log in.
1. The users should be able to make maintenance or repairs request.
1. An admin should be able to approve/reject a repair/maintenance request.
1. The admin should be able to mark request as resolved once it is done.
1. The admin should be able to view all maintenance/repairs requests on the application
1. The admin should be able to filter requests
1. The user can view all his/her requests
## Installation and setup
For installation and setup of the application have the following installed
1.git to access the repo
2.virtualenv to create a virtual environment
### Clone the repo
```bash
  git clone https://github.com/ronaldndirangu/Maintenance-Tracker.git
```
### Navigate to the root directory.
```bash
  cd Maintenance-Tracker/
```
### Create virtual environment
On linux
```bash
  python3 -m venv venv
```
On windows
```bash
  py -3 -m venv venv
```
### Activate virtual environment
On linux
```bash
  source venv/bin/activate
```
On windows
```bash
  \Python3\Scripts\virtualenv.exe venv
```
### Install dependancies
On your shell run
```bash
  pip install -r requirements.txt
```
### Running the application
```bash
  python3 run.py
```
### Endpoints
All endpoints can be accessed using the following url using curl or postman
```bash
  http://127.0.0.1/api/v1/
```
Below are the available endpoints

Endpoint | Task
------------ | -------------
POST /api/v1/users/login | User can login to the application
POST /api/v1/users/signup | User can signup for the application
POST /api/v1/users/request/ | User can create a request
GET /api/v1/users/request | User can view his/her requests
PUT /api/v1/users/request/<requestid> | User can edit a specific request
GET /api/v1/users/request/<requestid> | User view a specific request
DELETE /api/v1/users/request/<requestid> | User can delete a specific request
  
### Testing
To test the application run the following command on your shell
```bash
  pytest -v
```


