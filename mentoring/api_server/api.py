from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def mentoring():
    if request.method == "GET":
        print(request)
        # user = request.args.get('email')
        # print(user)
    return 'Hello, World!'
    
if __name__ == '__main__':
  app.run()