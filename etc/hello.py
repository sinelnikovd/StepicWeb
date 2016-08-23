def app(environ, start_response):
	data = environ["QUERY_STRING"]
	status = '200 OK'
	response_headers = [
		('Content-type','text/plain')
	]
	start_response(status, response_headers)
	return [data]