from flask import Blueprint,render_template,url_for,redirect
from flask_login import current_user, login_required,logout_user
from .models import Event
from .forms import EventForm
bp = Blueprint('main', __name__)


@bp.route('/')
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

@bp.route('/filter', methods=['POST', 'GET'])
def filter_events(genre):
    if Event.genre("<genre>"):
        curl = mysql.connection.cursor()
        curl.execute("SELECT * FROM events WHERE genre %s", [condition])
        data = curl.fetchall()
        curl.close()
        return render_template("/filter", events=data)
    else:
        return redirect(url_for('/index.html'))

@bp.route('/showall', methods=['POST'])
def showall():
    return filter_events(None)

@bp.route('/jazz', methods=['POST'])
def jazz():
    return filter_events('Jazz')

@bp.route('/pop', methods=['POST'])
def pop():
    return filter_events('Pop')

@bp.route('/rock', methods=['POST'])
def rock():
    return filter_events('rock')

@bp.route('/kpop', methods=['POST'])
def kpop():
    return filter_events('K-Pop')

@bp.route('/jpop', methods=['POST'])
def jpop():
    return filter_events('J-Pop')

@bp.route('/cpop', methods=['POST'])
def cpop():
    return filter_events('C-Pop')

@bp.route('/others', methods=['POST'])
def others():
    return filter_events('Others')

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
