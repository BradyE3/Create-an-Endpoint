from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    if slack_name is None or track is None:
        return jsonify({'error': 'Require both parameters'}), 400

    current_day = datetime.datetime.utcnow().strftime('%A')
    current_utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    github_file = 'https://github.com/BradyE3/Create-an-Endpoint'
    github_source = 'https://github.com/BradyE3/Create-an-Endpoint/blob/main/main.py'


    result = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': current_utc_time,
        'track': track,
        'github_file_url': github_file,
        'github_repo_url': github_source,
        'status_code': 200,
    }

    return jsonify(result)








if __name__ == '__main__':
    app.run(debug=True)