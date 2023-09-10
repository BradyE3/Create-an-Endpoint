from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def info():
    slack_name = request.args.get('Brady Ellison')
    track = request.args.get('backend')

    if param1 is None or param2 is None:
        return jsonify({'error': 'Require both parameters'}), 400

    current_day = datetime.datetime.utcnow().strftime('%A')
    current_utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    github_file = ''
    github_source = ''


    result = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': current_utc_time,
        'track': track,
        'github_file_url': '',
        'github_repo_url': '',
        'status_code': '200',
    }

    return jsonify(result)








if __name__ == '__main__':
    app.run(debug=True)