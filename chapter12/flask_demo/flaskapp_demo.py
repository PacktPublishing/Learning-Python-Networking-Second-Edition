#!/usr/local/bin/python3

from flask import Flask, abort

app = Flask(__name__)
app.debug = True
objs = __builtins__.__dict__.items()

docstrings = {name.lower(): obj.__doc__ for name, obj in objs if
name[0].islower() and hasattr(obj, '__name__')}

@app.route('/')
def index():
	link_template = '<a href="/functions/{}">{}</a></br>'
	links = []
	for func in sorted(docstrings):
		link = link_template.format(func, func)
		links.append(link)
	links_output = '\n'.join(links)
	return '<h1>Python builtins docstrings</h1>\n' + links_output

@app.route('/functions/<func_name>')
def show_docstring(func_name):
	func_name = func_name.lower()
	if func_name in docstrings:
		output = '<h1>{}</h1>\n'.format(func_name)
		output += '<pre>{}</pre>'.format(docstrings[func_name])
		return output
	else:
		abort(404)

if __name__ == '__main__':
	app.run()