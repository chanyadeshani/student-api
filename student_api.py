from flask import Flask, request
from flask_restful import reqparse, Resource, Api
import psycopg2
from datetime import datetime
import model
import student_service
import uuid

parser = reqparse.RequestParser()
parser.add_argument('id', type=str)
parser.add_argument('name', type=str)
parser.add_argument('birthday', type=str)


class Student(Resource):
    def get(self):
        args = parser.parse_args()
        student_id = args['id']
        student = student_service.get_student(student_id)

        return (student.id, student.name, student.birthday.strftime('%Y-%m-%d')), 200

    def post(self):
        args = parser.parse_args()
        student = model.Student(str(uuid.uuid4()), args['name'])
        student.birthday = datetime.strptime(args['birthday'], '%Y-%m-%d')
        return student_service.add_student(student), 201

    def put(self):
        args = parser.parse_args()
        student = model.Student(args['id'], args['name'])
        student.birthday = datetime.strptime(args['birthday'], '%Y-%m-%d')
        student_service.update_student(student)
        return 200

    def delete(self):
        args = parser.parse_args()
        student_id = args['id']
        student_service.delete_student(student_id),
        return 201
