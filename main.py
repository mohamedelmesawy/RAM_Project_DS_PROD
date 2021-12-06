from flask import Flask
import mlflow
import mlflow.sklearn
import CustomLinearRegression


# ML-FLOW set to your server URI
mlflow.set_tracking_uri('http://127.0.0.1:5000')
mlflow.set_experiment("/RAM-experiment")


app = Flask(__name__)


@app.route("/")
def hello():
    return("This is RAM Project for Data Science in production!")


@app.route("/prediction")
def prediction():
    score, model = CustomLinearRegression.train_and_evaluate(normalize=True)

    with mlflow.start_run():
        mlflow.log_param("LR-normalize", True)
        mlflow.log_metric("R2-score", score)

        # Logging training code
        mlflow.log_artifact(local_path='./data/Mall_Customers.csv')
        # Logging model to MLFlow
        mlflow.log_artifact(local_path='./CustomLinearRegression.py')
        mlflow.sklearn.log_model(sk_model=model,
                                 artifact_path='LR-Model')

    return("R2-Score: {:.2%}".format(score))


@ app.route("/admin")
def hello_admin():
    return("Admin page!")


app.run(debug=True, use_debugger=False, use_reloader=False, port=9000)
