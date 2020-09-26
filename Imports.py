import os

from PIL import Image

# from tqdm import tqdm



import time
from time import localtime, strftime
import base64
import io
import os
import numpy as np

import json
import uuid
from flask import request
from flask import jsonify, make_response
from flask import Flask, url_for, flash
from flask import render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL
from flask_login import LoginManager
from flask_login import UserMixin
from flask_login import login_user, current_user, logout_user, login_required
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms import Form, StringField, TextAreaField, PasswordField, SubmitField
from datetime import datetime
from werkzeug.utils import secure_filename
#
#
#
# from flask_socketio import SocketIO
# from flask_socketio import send, emit
# from flask_socketio import join_room, leave_room
