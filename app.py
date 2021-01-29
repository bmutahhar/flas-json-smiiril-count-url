import requests
from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    try:
        url = "https://www.instagram.com/graphql/query/?query_hash=37479f2b8209594dde7facb0d904896a&variables=%7B" \
              "%22id%22%3A%22256744793%22%2C%22first%22%3A12%7D "
        user_agent = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=user_agent)
        data = resp.json()
        try:
            number = data['data']['user']['edge_followed_by']['count']
        except KeyError:
            number = None
        if number is not None:
            return {'number': number}
        else:
            return {'error': "Count not found in the API"}
    except Exception as e:
        return {'error': str(e)}


if __name__ == "__main__":
    app.run(debug=True)
