from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    start_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    end_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    food_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)


class Food(db.Model):
    __tablename__ = 'food'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=False, nullable=False)
    quantity = db.Column(db.Integer)
    unit_price = db.Column(db.Integer)
    item_category = db.Column(db.String(150), unique=False, nullable=False)
