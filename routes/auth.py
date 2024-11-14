from flask import Blueprint, request, redirect, render_template, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from config import db

auth_bp = Blueprint('auth', __name__)

#Registration Route
