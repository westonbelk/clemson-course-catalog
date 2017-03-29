from flask import Flask, render_template, request
import json
import math
from functional import seq
from Course import Course


app = Flask(__name__)


#
# Load courses
#
courses = []
with open('data/courses.json') as f:
	courses = list(map(
		lambda c: Course(c),
		json.loads(f.read())
	))


#
# Routes
#
@app.route('/')
def index():
	return render_template('index.html')


@app.route('/subject/<subject>', methods=['GET'])
def subject(subject):
	return render_template('courses.html', courses=seq(courses)
		.filter(lambda c: c.subject == subject))


@app.route('/query', methods=['GET'])
def query():
	if(len(request.args) == 0):
		return render_template('query.html')

	subject = request.args.get('subject')
	min_query_number = request.args.get('min')
	max_query_number = request.args.get('max')
	title = request.args.get('title')
	instructor = request.args.get('instructor')

	if max_query_number == None or max_query_number == '':
		max_query_number = math.inf
	else:
		max_query_number = int(max_query_number)

	if min_query_number == None or min_query_number == '':
		min_query_number = 0
	else:
		min_query_number = int(min_query_number)

	return render_template('courses.html', courses=seq(courses)
		.filter(lambda c: subject == None or subject == '' or c.subject.lower() == subject.lower())
		.filter(lambda c: c.number >= min_query_number)
		.filter(lambda c: c.number <= max_query_number)
		.filter(lambda c: title == None or title == '' or title.lower() in c.title.lower())
		.filter(lambda c: instructor == None or instructor == '' or any(map(lambda t: instructor.lower() in t.name.lower() , c.instructors))))
