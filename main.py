from flask import Flask
import mlflow
import model


# ML-FLOW set to your server URI
mlflow.set_tracking_uri('http://127.0.0.1:5000')
mlflow.set_experiment("/RAM-experiment")


app = Flask(__name__)


@app.route("/")
def hello():
    return("This is RAM Project for Data Science in production!")


@app.route("/prediction")
def prediction():
    score = model.train_and_evaluate(normalize=True)
    with mlflow.start_run():
        mlflow.log_param("LR-normalize", True)
        mlflow.log_metric("R2-score", score)
    return("R2-Score: {:.2%}".format(score))


@app.route("/admin")
def hello_admin():
    return("Admin page!")


app.run(debug=True, use_debugger=False, use_reloader=False, port=9000)
