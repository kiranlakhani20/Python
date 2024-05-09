from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/cmd')
def cmd():
    cmd = request.args.get("cmd", "whoami")
    status = os.system(cmd)
    return str(status == 0)

if __name__ == '__main__':
    app.run()
