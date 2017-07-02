

def wsgi_application(environ, start_response):
	status = '200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]
	body = ''
	for i in environ:
		body += str(i) + '\n'
	
	start_response(status, headers)
	return [body]