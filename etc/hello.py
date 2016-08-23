bind = "127.0.0.1:8080"
def app(environ, start_response):
	data = environ["QUERY_STRING"]
	status = '200 OK'
	response_headers = [
		('Content-type','text/plain')
	]
	start_response(status, response_headers)
	return [data]