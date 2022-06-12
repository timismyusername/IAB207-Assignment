from flask import Blueprint,render_template,url_for,redirect
from .models import Event

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    event = Event.query.all()    
    return render_template('index.html', event=event)