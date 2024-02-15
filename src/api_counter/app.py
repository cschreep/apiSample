from flask import Flask

from api_counter.blueprints.api_blueprint import api
from api_counter.blueprints.stats_blueprint import stats
from api_counter.blueprints.test_blueprint import test

app = Flask(__name__)

app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(stats, url_prefix="/stats")
app.register_blueprint(test, url_prefix="/test")

if __name__ == "__main__":
    app.run()
