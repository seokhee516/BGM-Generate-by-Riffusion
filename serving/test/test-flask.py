from flask import Flask

def create_app():

	app = Flask(__name__)

	@app.route("/")
	def index():
		return "Hello, World!", 200

	return app

if __name__ == "__main__":
	app = create_app()
	app.run(host='0.0.0.0', port=5000, debug=True)