from bottle import route, template, run, static_file, request, response
import json
import requests



@route('/create_ticket', method=['GET', 'POST'])
def handle_form():
    if 'verified_email' in request.cookies:
        ask_email = False
    else:
        ask_email = True
    status = ''
    if request.POST:
        # Get the form data
        subject = request.forms.get('subject')
        description = request.forms.get('description')
        if 'verified_email' in request.cookies:
            email = request.get_cookie('verified_email')
        else:
            email = request.forms.get('email')
        # Package the data for the API
        data = {'request': {'subject': subject, 'comment': {'body': description}}}
        ticket = json.dumps(data)
        # Make the API request
        user = email + '/token'
        api_token = 'hLWJTPCI6vXxIFjGcT6XnxDpG7MnfVSehNy7RZLP'
        url = 'https://zendeskcodingchallenge8643.zendesk.com/api/v2/requests.json'
        headers = {'content-type': 'application/json'}
        r = requests.post(
            url,
            data=ticket,
            auth=(user, api_token),
            headers=headers
        )
        if r.status_code != 201:
            if r.status_code == 401 or 422:
                status = 'Could not authenticate you. Check your email address or register.'
                ask_email = True
            else:
                status = 'Problem with the request. Status ' + str(r.status_code)
            return status
        else:
            status = 'Ticket was created. Look for an email notification.'
            if 'verified_email' not in request.cookies:
                response.set_cookie('verified_email', email, max_age=364*24*3600)
                ask_email = False
    return template('ticket_form', feedback=status, no_email=ask_email)

'''
@route('/get_all_tickets', method=['GET', 'POST'])
def handle_form2():
    if 'verified_email' in request.cookies:
        ask_email = False
    else:
        ask_email = True
    status=''
    if request.GET:
        if 'verified_email' in request.cookies:
            email = request.get_cookie('verified_email')
        else:
            email = request.forms.get('email')
        user = email + '/token'
        api_token = 'hLWJTPCI6vXxIFjGcT6XnxDpG7MnfVSehNy7RZLP'
        url='https://zendeskcodingchallenge8643.zendesk.com/api/v2/tickets.json'
        all_tickets=requests.get(url, auth=(user, pwd))
        python_data = all_tickets.json()
        if json_all_tickets.status_code != 201:
            if json_all_tickets.status_code == 401 or 422:
                status = 'Could not authenticate you. Check your email address or register.'
                ask_email = True
            else:
                status = 'Problem with the request. Status ' + str(json_all_tickets.status_code)
            return status
        else:
            print(python_data)
            status = 'Ticket was created. Look for an email notification.'
            if 'verified_email' not in request.cookies:
                response.set_cookie('verified_email', email, max_age=364*24*3600)
                ask_email = False
        
    return template('get_form', no_email=ask_email);
'''

@route('/css/<filename>')
def send_css(filename):
    return static_file(filename, root='static/css')


run(host='localhost', port=8080, debug=True)
