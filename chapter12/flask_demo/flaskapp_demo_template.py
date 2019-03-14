#!/usr/local/bin/python3

from flask import Flask, abort, render_template

app = Flask(__name__)
app.debug = True
objs = __builtins__.__dict__.items()

docstrings = {name.lower(): obj.__doc__ for name, obj in objs if
name[0].islower() and hasattr(obj, '__name__')}

@app.route('/')
def index():
	return render_template('index.html', funcs=sorted(docstrings))

@app.route('/functions/<func_name>')
def show_docstring(func_name):
	func_name = func_name.lower()
	if func_name in docstrings:
		return render_template('docstring.html', func_name=func_name, doc=docstrings[func_name])
	else:
		abort(404)

if __name__ == '__main__':
	app.run()