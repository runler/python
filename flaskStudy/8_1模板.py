from flask import Flask,render_template


app = Flask(__name__)


@app.route("/index")
def index():
	# return render_template("index.html", name="python", age=18) # 直接平铺传参数

	data = {
		"name": "python",
		"age": 17,
		"my_dict": {"city": "sz"},
		"my_list": [1, 2, 3, 4, 5],
		"my_int": 0
	}
	return render_template("index.html", **data)  # 字典传参数


if __name__ == '__main__':
	app.run(Debug=True)