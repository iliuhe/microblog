from app import app, db
from app.models import User, Post

# the @ registers the function as a shell context function
# when flask shell runs, it will invoke this function and register the items
@app.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User, 'Post': Post}
