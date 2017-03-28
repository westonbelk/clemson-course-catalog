import datetime

class Instructor:
	name = ""
	email = ""
	primary = False

	def __init__(self, obj):
		self.name = obj['displayName']
		self.email = obj['emailAddress']
		self.primary = obj['primaryIndicator']

class MeetingTime:
	start_time = ""
	end_time = ""
	building = ""
	days_of_week = []

	def __init__(self, obj):
		self.start_time = datetime.datetime.strptime(obj['beginTime'], "%H%M") if obj['beginTime'] != None else None
		self.end_time = datetime.datetime.strptime(obj['endTime'], "%H%M") if obj['endTime'] != None else None
		self.building = obj['buildingDescription']
		self.days_of_week = [obj['sunday'], obj['monday'], obj['tuesday'], obj['wednesday'], obj['thursday'], obj['friday'], obj['saturday']]

class Course:
	subject = ""
	number = 0
	title = ""
	meeting_times = []
	instructors = []
	section = ""
	crn = ""

	def __init__(self, obj):
		self.subject = obj['subject']
		self.number = int(obj['courseNumber'])
		self.title = obj['courseTitle']
		self.meeting_times = list(map(lambda m: MeetingTime(m['meetingTime']), obj['meetingsFaculty']))
		self.instructors = list(map(lambda p: Instructor(p), obj['faculty']))
		self.section = obj['sequenceNumber']
		self.crn = obj['courseReferenceNumber']

