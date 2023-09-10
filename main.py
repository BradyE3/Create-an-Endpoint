from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():

    slack_name = request.args.get('slack_name')
    track = request.args.get('track')


    if slack_name is None or track is None:
        return jsonify({'error': 'Both slack_name and track parameters are required'}), 400


    current_day = datetime.datetime.utcnow().strftime('%A')
    current_utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')


    github_file_url = 'https://github.com/yourusername/yourrepository/blob/main/yourfile.py'
    github_source_code_url = 'https://github.com/yourusername/yourrepository'


    response = {
        'slack_name': slack_name,
        'current_day': current_day,
        'current_utc_time': current_utc_time,
        'track': track,
        'github_file_url': github_file_url,
        'github_source_code_url': github_source_code_url,
        'status_code': 200
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
