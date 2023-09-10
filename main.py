from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slack_name = db.Column(db.String(255), nullable=False)
    track = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

@app.route('/api', methods=['GET'])
def api():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Check if both parameters are provided
    if slack_name is None or track is None:
        return jsonify({'error': 'Both slack_name and track parameters are required'}), 400

    # Get the current day of the week and UTC time
    current_day = datetime.datetime.utcnow().strftime('%A')
    current_utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    # Mock GitHub URLs (replace with actual URLs)
    github_file_url = 'https://github.com/yourusername/yourrepository/blob/main/yourfile.py'
    github_source_code_url = 'https://github.com/yourusername/yourrepository'

    with app.app_context():
        # Create a new user record in the database
        user_info = UserInfo(slack_name=slack_name, track=track)
        db.session.add(user_info)
        db.session.commit()

    # Create the response JSON
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
    with app.app_context():
        db.create_all()  # Create the database schema
    app.run(debug=True)
