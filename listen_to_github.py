from flask import json,request,Flask

app=Flask(__name__)

@app.route('/')
def api_root():
    return 'welcom guys'


@app.route('/github', methods=['POST'])
def app_gh_message():
    if request.headers['Content-Type']=='application/json':
        my_info=json.dumps(request.json)
        print(my_info)
        return my_info

