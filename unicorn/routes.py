import time

import psutil

from unicorn.app import app
from flask import render_template, send_from_directory, request, jsonify

import requests
import json


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/static/<path:path>')
def statics(path):
    return send_from_directory('static', path)


@app.route('/plugins/<path:path>')
def plugins(path):
    return send_from_directory('static/plugins', path)


@app.route("/_submit_task")
def _submit_task():
    req_str = request.args.get('text')
    r = requests.post(app.config["SUBMIT_TASK_URL"], data=req_str, headers={'content-type': 'application/json'})
    return jsonify(result=r.text)


@app.route("/_calculate_bandwidth")
def _calculate_bandwidth():
    req_str = request.args.get('text')
    r = requests.post(app.config["CALCULATE_BANDWIDTH_URL"], data=req_str, headers={'content-type': 'application/json'})
    return jsonify(result=r.text)


@app.route("/_calculate_bandwidth_interdomain")
def _calculate_bandwidth_interdomain():
    r = {
        "flows": [
            {
                "flow-id": 1,
                "bandwidth": 40000
            },
            {
                "flow-id": 2,
                "bandwidth": 40000
            }
        ]
    }
    return jsonify(result=json.dumps(r))


@app.route("/_run_task")
def _run_task():
    req_str = request.args.get('text')
    r = requests.post(app.config["RUN_TASK_URL"], data=req_str, headers={'content-type': 'application/json'})
    return jsonify(result=r.text)

@app.route("/_run_task_interdomain")
def _run_task_interdomain():
    req_str = request.args.get('text')
    r = requests.post(app.config["RUN_TASK_INTERDOMAIN_URL"], data=req_str, headers={'content-type': 'application/json'})
    return jsonify(result=r.text)


@app.route("/_stop_task")
def _stop_task():
    r = requests.post(app.config["STOP_TASK_URL"])
    return jsonify(result=r.text)


@app.route("/_on_demand_pce")
def _on_demand_pce():
    req_str = request.args.get('text')
    r = requests.post(app.config["ON_DEMAND_PCE_URL"], data=req_str, headers={'content-type': 'application/json'})
    return jsonify(result=r.text)


@app.route("/_resource_query")
def _resource_query():
    req_str = request.args.get('text')
    r = requests.post(app.config["RESOURCE_QUERY_URL"], data=req_str, headers={'content-type': 'application/json'})
    return jsonify(result=r.text)


@app.route("/_resource_query_interdomain")
def _resource_query_interdomain():
    req_str = request.args.get('text')
    data = json.loads(req_str)
    ingress_points = data["query-desc"][0]["ingress-point"]
    if ingress_points == "":
        r = {
            "ane-matrix": [
                [{"flow-id": 1}, {"flow-id": 2}]
            ],
            "anes": [
                {"availbw": 100000}
            ]
        }
        return jsonify(result=json.dumps(r))
    elif ingress_points.split('.')[2] == '1':
        r = {
            "ane-matrix": [
                [{"flow-id": 1}, {"flow-id": 2}]
            ],
            "anes": [
                {"availbw": 40000}
            ]
        }
        return jsonify(result=json.dumps(r))
    else:
        r = {
            "ane-matrix": [
                [{"flow-id": 1}, {"flow-id": 2}]
            ],
            "anes": [
                {"availbw": 100000}
            ]
        }
        return jsonify(result=json.dumps(r))


@app.route("/_network_data")
def _network_data():
    network_data_start = psutil.net_io_counters(pernic=True)
    time.sleep(app.config["MONITORING_INTERVAL"])
    network_data = psutil.net_io_counters(pernic=True)

    data = {}

    for intf in network_data:
        data[intf] = {
            "sent_bytes_sec": (network_data[intf][0] - network_data_start[intf][0] / app.config["MONITORING_INTERVAL"]),
            "received_bytes_sec": (
                    network_data[intf][1] - network_data_start[intf][1] / app.config["MONITORING_INTERVAL"])
        }

    return json.dumps(data)


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


def apply_routes(app):
    """
    You need to import this module after initializing app
    """
    pass
