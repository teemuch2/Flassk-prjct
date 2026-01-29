from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# Load dataset
data = pd.read_csv("employee_data.csv")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/attrition-rate")
def attrition_rate():
    total = len(data)
    yes = len(data[data["Attrition"] == "Yes"])
    no = len(data[data["Attrition"] == "No"])
    rate = (yes / total) * 100

    return jsonify({
        "total": total,
        "yes": yes,
        "no": no,
        "rate": round(rate, 2)
    })

@app.route("/department-attrition")
def department_attrition():
    dept = data[data["Attrition"] == "Yes"].groupby("Department").size()
    return jsonify(dept.to_dict())

if __name__ == "__main__":
    app.run(debug=True)
