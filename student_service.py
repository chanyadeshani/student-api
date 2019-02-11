import datetime

import psycopg2
import model


def get_connection():
    try:
        return psycopg2.connect("dbname='myschool' user='myuser' host='localhost' password='password'")
    except (Exception, psycopg2.DatabaseError) as e:
        print("I am unable to connect to the database", e)


def get_student(id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("select * from student where id = %s", (id,))
        student = cursor.fetchone()
        return_student = model.Student(student[0], student[1])
        return_student.birthday = student[2]
        return return_student
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def add_student(student):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        student_insert_query = "insert into student (ID, NAME, BIRTHDAY) values (%s, %s, %s) RETURNING id"
        student_to_insert = (student.id, student.name, student.birthday.strftime('%Y-%m-%d'))

        cursor.execute(student_insert_query, student_to_insert)

        conn.commit()

        count = cursor.rowcount
        if count == 1:
            return_id = cursor.fetchone()
            return return_id
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def update_student(student):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("update student set birthday = %s, name = %s  where id = %s", (student.birthday, student.name, student.id))
        conn.commit()

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def delete_student(id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("delete from student where id = %s",(id,))
        conn.commit()

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
