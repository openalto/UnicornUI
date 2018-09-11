from flask import Flask

app = Flask(__name__)

app.config["SUBMIT_TASK_URL"] = "http://127.0.0.1:6666/tasks"
app.config["CALCULATE_BANDWIDTH_URL"] = "http://127.0.0.1:6666/calculate_bandwidth"
app.config["RUN_TASK_URL"] = "http://127.0.0.1:6666/run_task"
app.config["RUN_TASK_INTERDOMAIN_URL"] = "http://127.0.0.1:6666/run_task_interdomain"
app.config["STOP_TASK_URL"] = "http://127.0.0.1:6666/stop_task"
app.config["ON_DEMAND_PCE_URL"] = "http://127.0.0.1:6666/on_demand_pce"
app.config["RESOURCE_QUERY_URL"] = "http://127.0.0.1:6666/resource_query"
app.config["MONITORING_INTERVAL"] = 1
