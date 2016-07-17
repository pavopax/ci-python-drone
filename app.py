import os
from flask import Flask, request, render_template

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

# controllers
# @app.route("/")
# def hello():
#     return "Hello from Python!"

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        uu = Upload()
        for inputName in request.files:
            for upload in request.files.getlist(inputName):
                app.logger.debug(secure_filename(upload.filename))
                upload.save(os.path.join('/tmp/demo', secure_filename(upload.filename)))
    return render_template('templates/index.html')

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
