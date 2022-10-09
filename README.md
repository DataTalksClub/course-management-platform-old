# Course Management Platform

A platform for hosting our courses

## Running it locally

### Installing dependencies

Install pipenv:

```bash
pip install pipenv
```

Install the dependencies:

```bash
pipenv install
```

Activate virtual env:

```bash
pipenv shell
```

### Prepare the service

```bash
cd cmp
```

Make migrations:

```bash
python manage.py migrate
```

Add an admin user:

```bash
python manage.py createsuperuser
```

Go to the admin panel, and add

* A new site: `127.0.0.1:8000` - note the site ID
* Secrets and keys for OAuth


### Running the service

And run it:

```bash
export SITE_ID=4
python manage.py runserver 0.0.0.0:8000
```

Where `SITE_ID` is the ID of the `127.0.0.1:8000` site

