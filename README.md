# Getting Started

The purpose of this project is to allow a developer to quickly get started with FastAPI, SQLAlchemy, and the DigitalOcean Apps Platform. Supported functionality includes basic user management, an example notes API, and a simple healthcheck that connects to the database (this endpoint should be protected in production).

**Note: Following these steps will result in charges for the use of DigitalOcean services**

# Requirements

You need a DigitalOcean account. If you don't already have one, you can sign up at https://cloud.digitalocean.com/registrations/new.
    
# Deploying the App

Click this button to deploy the app to the DigitalOcean App Platform.

 [![Deploy to DO](https://mp-assets1.sfo2.digitaloceanspaces.com/deploy-to-do/do-btn-blue.svg)](https://cloud.digitalocean.com/apps/new?repo=https://github.com/justinrmiller/fastapi-sqlalchemy-doapp/tree/main)

# Mac Instructions

Make sure to install the following (brew commands as examples):

```
    brew install postgresql
    brew install libpq
```

Also have the Rust compiler installed for crypto. You should be able to install it via RustUp.

# Running locally

Follow the following steps:

1. Add the following to `.env` in the base directory (generate secret key with `openssl rand -hex 32`):
   ```
   SECRET_KEY="<secret key here>"
   GUNICORN_WORKERS=4
   ENV=dev
   VERSION=1.0.0
   ```
2. Generate certs first using `generate_certs.sh`
3. Run `make build`
4. Run `make run`


# Steps to Deploy:

Note: Make sure to set the following env variables 

- SECRET_KEY (generate this using `openssl rand -hex 32`, set this in your .env file)
- DATABASE_URL (available in the app after first deploy) in DigitalOcean for the app
- ENV (environment you're operating in, e.g. 'stage', 'prod')
- VERSION (version number of your application)

Then follow these steps:

1. Authorize with DigitalOcean:
    - `doctl auth init`

2. Create the application using the app yaml (this will store the returned ID in .app-id).
    - `doctl apps create --spec ./.do/app.yaml --format ID --no-header > .app-id`

3. List applications:
    - `doctl apps list --format "Spec.Name, ID"`

4. Update the application as needed using the ID in .app-id
    - `doctl apps update <app-id here>`

5. Delete the application to avoid charges.
	- `doctl apps delete <app-id here> && rm .app-id`

