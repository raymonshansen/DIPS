# To-DO list

A simple to-DO list for DIPS summer Internships Summer 2019

## Getting Started

Clone or copy the repo.

### Prerequisites

I used the pytest testig framework to test the code. Install with:

```
pip3 --user install pytest pytest-spec
```
Flake 8 is used to conform to PEP8-guide. To install flake 8:
```
pip3 --user install flake8
```
Solution is written in python 3.6

## Running the tests

Running the tests for this solution can be done with:
```
pytest --spec
```
or:
```
python3 todo_test.py
```

### Coding style tests

Test if coding style conforms to pythons PEP8 guide.
From DIPS folder, run:

```
flake8 .
```

## Deployment

Run the app with:
```
python3 todo_app.py
```