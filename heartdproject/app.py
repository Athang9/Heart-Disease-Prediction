from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route("/signin")
def sign():
	return render_template("sign.html")

@app.route("/login")
def sign():
	return render_template("sign.html")

@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/find")
def find():
	age = float(request.args.get("age"))
	bp = float(request.args.get("bp"))
	chole = float(request.args.get("chole"))
	hr = float(request.args.get("hr"))
	peak = float(request.args.get("peak"))
	r1 = request.args.get("r1")
	if r1 == "no":
		exe = 0
	else:
		exe = 1
	r2 = request.args.get("r2")
	if r2 == "u":
		stf = 0
		stu = 1
	elif r2 == "f":
		stf = 1
		stu = 0
	else:
		stf = 0
		stu = 0
	with open("heart.model", "rb") as f:
		model = pickle.load(f)
	data = [[age, bp, chole, hr, peak, exe, stf, stu]]
	res = model.predict(data)
	res1 = res[0]
	if res1 == 1:
		msg = "Heart Disease is Detected"
	else:
		msg = "Heart Disease is not Detected"
	
	return render_template("home.html", m=msg)

if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)	