# Dockerizing Flask with Postgres, Gunicorn, and Nginx

## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx).

## Want to use this project?

### Development

Uses the default Flask development server.

1. create env files .env.dev
1. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
1. Build the images and run the containers:

    ```sh
    $ sudo docker-compose up -d --build
    ```

    Test it out at [http://localhost:5000](http://localhost:5000). The "web" folder is mounted into the container and your code changes apply automatically.

### Production

Uses gunicorn + nginx.

1. create env files .env.prod and .env.prod.db.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost](http://localhost). No mounted folders. To apply changes, the image must be re-built.
1. Build db
    ```sh
    $ sudo docker exec -it construction-of-guts_web_1 python manage.py create_db
    ```
1. Create admin user
    ```shell script
    $ sudo docker exec -it construction-of-guts_web_1 python manage.py create_admin_user
    ```
1. Fill the database tables by clicking on the link 
    ```http request
    http://HOSTNAME:PORT/api/protect/fill_tables
    ```
1. Fill the Length TU table by clicking on the link 
    ```http request
    http://HOSTNAME:PORT/api/protect/fill_length_tu_table
    ```