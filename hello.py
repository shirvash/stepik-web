def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    query = env['QUERY_STRING'].split('&')
    result = [];
    
    for param in query:
        result.append(param + "\n")
        
    return result