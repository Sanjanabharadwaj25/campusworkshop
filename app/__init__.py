"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7ll64dadc9vlud380-a.oregon-postgres.render.com",
        database="todo_51jv",
        user="todo_51jv_user",
        password="79Ih17cyTaDk6I8W90RGUsJzww0y4flN")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
