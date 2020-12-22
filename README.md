# ActiveMQ Artemis Console test suite

Maintainers: dlenoch <dlenoch@redhat.com>

## Requirements

- Python 3.6 or higher
- Browser driver Gecko, Chrome.. (look for Selenium drivers) 

## How to run

### Use pipenv
Is the best way how to run this tests

#### Setup your environment
```bash
pipenv install
```

#### Activate pipenv shell
```bash
pipenv shell
```

### Run the test suite
```bash
py.test --base-url http://172.28.1.1:8161/console --driver Chrome --variables settings.json
```