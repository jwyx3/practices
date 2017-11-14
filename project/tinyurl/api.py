from flask import Flask, url_for
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('api_key')
parser.add_argument('url', required=True)
parser.add_argument('custom_alias')
parser.add_argument('expired_at')


# simulate Cassandra
cassandra = {}

# helper
def get_short_id():
    return 'xxx'


class CreateUrl(Resource):
    def post(self):
        args = parser.parse_args()
        short_id = get_short_id()
        cassandra[short_id] = {'url': args['url']}
        return {'short_url': url_for('geturl', short_id=short_id, _external=True)}, 201


class GetUrl(Resource):
    def get(self, short_id):
        if short_id in cassandra:
            return {}, 301, {'Location': cassandra[short_id]['url']}
        abort(404, description=f'/{short_id} is not found')

# routing
api.add_resource(CreateUrl, '/shorten')
api.add_resource(GetUrl, '/<short_id>')

if __name__ == '__main__':
    app.run(debug=True)

