def app(environ, start_response):
	status = '200 OK'
	response_headers = [
		('Content-type','text/plain')
	]
	data = environ['QUERY_STRING'].replace('&','\n')
	start_response(status, response_headers)
	return [data]