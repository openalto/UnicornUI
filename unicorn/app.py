from flask import Flask

app = Flask(__name__)

app.config["SUBMIT_TASK_URL"] = "http://127.0.0.1:6666/tasks"
app.config["CALCULATE_BANDWIDTH_URL"] = "http://127.0.0.1:6666/calculate_bandwidth"
app.config["RUN_TASK_URL"] = "http://127.0.0.1:6666/run_task"
app.config["MONITORING_INTERVAL"] = 1
