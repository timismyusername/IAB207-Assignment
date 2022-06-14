from flask import Blueprint,render_template,url_for,redirect
from flask_login import current_user, login_required,logout_user
from .models import Event
from .forms import EventForm
bp = Blueprint('main', __name__)


@bp.route('/')
@login_required
def index():
    event = Event.query.all()    
    return render_template('index.html', event=event)

@bp.route('/search')
def search():
    if request.args['search']:
        print(request.args['search'])
        eve = "%" + request.args['search'] + '%'
        event = Event.query.filter(Event.description.like(eve)).all()
        return render_template('index.html', event=event)
    else:
        return redirect(url_for('main.index'))

@bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth.login'))

@bp.route('/creation', methods=['GET','POST'])
@login_required
def createEvent():
    createEvent_form = EventForm()
    return render_template(
        'creation.html', current_user=current_user,form=createEvent_form)

@bp.route('/history', methods=['GET','POST'])
@login_required
def history():
    """Logged-in User Dashboard."""
    return render_template(
        'book_history.html',
         current_user=current_user,
    )

@bp.route('/details', methods=['GET','POST'])
@login_required
def event_details():
    """Logged-in User Dashboard."""
    return render_template(
        'event_details.html',
        current_user=current_user
    )
