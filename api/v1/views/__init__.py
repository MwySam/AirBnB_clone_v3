#!/usr/bin/python 3

from flask import Flask, Blueprint
from api.v1.views.index import *
app = Flask(__name__)
app_views = Blueprint('app_views',__name__,url_prefix="/api/v1")

