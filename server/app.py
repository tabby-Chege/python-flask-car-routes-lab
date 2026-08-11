from flask import Flask

# Catalog of available Flatiron Cars models.
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

app = Flask(__name__)


@app.route('/')
def index():
    """Display the company landing page."""
    return 'Welcome to Flatiron Cars'


@app.route('/<model>')
def model_route(model):
    """Check whether the requested model exists in the fleet catalog."""
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    return f'No models called {model} exists in our catalog'


if __name__ == '__main__':
    app.run(debug=True)
