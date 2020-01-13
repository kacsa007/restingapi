from app.services.data_error_service import create_app

app = create_app()

if __name__ == '__main__':

    # One line to set the cache to a dictionary, and by doing so, removing the limit of the number of cached templates.
    app.jinja_env.cache = {}  # this line speeds up our application
    app.run()
