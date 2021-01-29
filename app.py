import json

import requests
from flask import Flask, Response

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    try:
        url = "https://www.instagram.com/graphql/query/?query_hash=37479f2b8209594dde7facb0d904896a&variables=%7B" \
              "%22id%22%3A%22256744793%22%2C%22first%22%3A12%7D "
        user_agent = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=user_agent)
        print("*" * 100)
        print("Status Code: ", resp.status_code)
        print(resp.text)
        print("*" * 100)
        data = json.loads(resp.text)
        print("*" * 100)
        print(data)
        print("*" * 100)
        try:
            number = data['data']['user']['edge_followed_by']['count']
        except KeyError:
            number = None
        if number is not None:
            return Response(response=json.dumps({'number': number}), status=200,
                            mimetype='application/json')
        else:
            return Response(response=json.dumps({'error': "Could not found count in the API"}), status=500,
                            mimetype='application/json')
    except Exception as e:
        print("*" * 100)
        print(data)
        print("*" * 100)
        return Response(response=json.dumps({'error': str(e)}), status=500,
                        mimetype='application/json')


if __name__ == "__main__":
    app.run(debug=True)
