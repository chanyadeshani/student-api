
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import student_api

app = Flask(__name__)


api = Api(app)

api.add_resource(student_api.Student, '/student')

if __name__ == '__main__':
    app.run()
