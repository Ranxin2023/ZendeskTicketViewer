#################################################################################################
# PROJECT: Intern Coding Challenge 
# PROJECT DEMANDING PAPER: Intern Coding Challenge---Zendesk Ticket Viewer
# DEADLINE: November 29th, 2022
# NAME : Zendesk Ticket Viewer
# DEMAND:
#	Connect to the Zendesk API
#	Request all the tickets for your account
#	Display them in a list
#	Display individual ticket details
#	Page through tickets when more than 25 are returned
from datetime import datetime
import time
import requests

# ###################################################################################################
# Function:gets tickets in a Zendesk according account
# Function by curl:curl https://{subdomain}.zendesk.com/api/v2/tickets.json -v -u {email_address}:{password}
# input:  
#    Username and password
# Output:
# 
# Return:
#
# Reference 
#   Ref1 Code: https://developer.zendesk.com/documentation/developer-tools/working-with-the-zendesk-apis/making-requests-to-the-zendesk-api/#topic_hdt_nfx_3m
#   Ref2 HTTP response status codes https://developer.zendesk.com/documentation/developer-tools/getting-started/rest-api-glossary/#http-response-status-codes
#             400 response codes in zendesk: https://developer.zendesk.com/api-reference/ticketing/introduction/#400-range
#   Ref3 Ticket Format Jason: https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/#json-format
#   Ref4 Ticket Format Get Curl: https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/#using-curl
#   Ref5 Ticket Response example: https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/#example-response
#   Ref6 Converting JSON to Python data:https://developer.zendesk.com/documentation/developer-tools/getting-started/working-with-json/#python
def getBulkData(user, pwd):
    url = 'https://zcczendeskcodingchallenge8643.zendesk.com/api/v2/tickets.json'
    #get the time before 
    timeStart_full=time.localtime()
    timeStart_float=time.time()
    timeStart_sec=time.strftime("%H:%M:%S", timeStart_full)
    timeStart_calculate=datetime.strptime(timeStart_sec, "%H:%M:%S")

    # Do the HTTP get request
    response = requests.get(url, auth=(user, pwd))
    # Check for HTTP codes other than 200
    if response.status_code != 200:
        if response.status_code==403:
            print('error '+str(response.status_code)+" Please restart Zendesk Tickets Viwer. If problem still exist, please contact Service Center: https://www.zendesk.com/contact/\n")
        elif response.status_code==401:
            print('error '+str(response.status_code)+' Could not authenticate you. Please check your username or password.')
        elif response.status_code==404:
            print('error '+str(response.status_code)+' an internal error has occurred.Please restart Tickets Viwer. '+
                  'If problem still exist, please contact Service Center: https://www.zendesk.com/contact/\n')
        return response.status_code
    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    totalTickets=data['count']
    data_list=[]
    data_list.append(data)

    #put the tickets of all pages in a list
    while data['next_page']:
        url=data['next_page']
        # Check for HTTP codes other than 200
        response = requests.get(url, auth=(user, pwd))
        data = response.json()
        data_list.append(data)
        
    #get the time after
    timeEnd_full=time.localtime()
    timeEnd_float=time.time()
    timeEnd_sec=time.strftime("%H:%M:%S", timeEnd_full)
    timeEnd_calculate=datetime.strptime(timeEnd_sec, "%H:%M:%S")
                
    loadtime_show=timeEnd_calculate-timeStart_calculate
    loadtime_calculate=timeEnd_float-timeStart_float
    receivedTickets=0
                
    for eachData in data_list:
        receivedTickets+=len(eachData['tickets'])
    percentReceived=int(receivedTickets/totalTickets*100)
    averageDLoad=int(receivedTickets/loadtime_calculate)
    return [totalTickets, percentReceived, receivedTickets, averageDLoad, loadtime_show, data_list]

# ###################################################################################################
# Function:Show Ticket list and detail of individual ticket
# input:  
#    Username and password
#    Conmand number
# Output:
#    All tickets list
#    Individual ticket detial 
# Exception:
#    Authentication fail : notice user check username and password
#    API unavailable or program error : notice user restart or call servie center
def ztViewer():
    
    print('Welcome to the Zendesk Ticket Viewer')
    user = input('Enter your username: ')
    pwd = input('Enter your password: ')
    #token:'hLWJTPCI6vXxIFjGcT6XnxDpG7MnfVSehNy7RZLP'
    
    dataReturned=[]
    whetherInput2=False
    
    
    while(True):
        print('*'*80)
        print('\t\tZendesk Ticket Viewer MENU')    
        print('\t * Press 1: Display all tickets in a list')
        print('\t * Press 2: Display individual ticket details')
        print("\t * Press 'quit' or 'q' to exit")
        print('*'*80)
        inputFromMenu=input();
        # Set the request parameters
            
        if inputFromMenu=='1':
            dataReturned=getBulkData(user, pwd)
            if type(dataReturned)==int:
                return dataReturned
            print('='*116)
            print("| Total   %  | Received   %  | Xferd  % |  Average Speed   |     Time     |      Time    |     Time    |  Current  |")
            print("|            |               |          |  Dload | Upload  |     Total    |      Spent   |     Left    |   Speed   |")
            if dataReturned[3]>=100:
                print("|  {0}   100 |   {2}     {1} |   0    0 |   {3}  |    0    |    {4}   |     {5}  |   --:--:--  |     {6}   |".
                  format(dataReturned[0],dataReturned[1],dataReturned[2],dataReturned[3],dataReturned[4], dataReturned[4], dataReturned[3]))
            else:
                print("|  {0}   100 |   {2}     {1} |   0    0 |   {3}   |    0    |    {4}   |     {5}  |   --:--:--  |     {6}    |".
                  format(dataReturned[0],dataReturned[1],dataReturned[2],dataReturned[3],dataReturned[4], dataReturned[4], dataReturned[3]))
            print('-'*116)
            print('\tTicket Subject \t\t\t\t\tOpener\t\t\t  Open time ')
            print('-'*116)
            for eachData in dataReturned[5]:
                for index in range(len(eachData['tickets'])):
                    #if more than 48 characters for the subject, cut the tail and add ... 
                    if len(eachData['tickets'][index]['subject'])>48:
                        subject=eachData['tickets'][index]['subject'][:47]
                        print(("'{0}'"+'... '+"{1} \t\t {2}").format(subject,eachData['tickets'][index]['requester_id'],eachData['tickets'][index]['updated_at']))
                    else:
                        print(("'{0}'"+' '*(51-len(eachData['tickets'][index]['subject']))+"{1} \t\t {2}").format(eachData['tickets'][index]['subject'],
                                                                                      eachData['tickets'][index]['requester_id'],eachData['tickets'][index]['updated_at']))
                    
                    if(index%25==24):
                        print()
                        input("...press any key to continue...\n")
        elif inputFromMenu=='2':
            while(True):
                print('Enter Ticket Number:')
                numOfTicket=input()
                
                
                url='https://zcczendeskcodingchallenge8643.zendesk.com/api/v2/tickets/'+numOfTicket+'.json'
                # Do the HTTP get request
                response = requests.get(url, auth=(user, pwd))

                # Check for HTTP codes other than 200
                if response.status_code != 200:
                    if response.status_code==403:
                        print('error '+str(response.status_code)+" Please restart Zendesk Tickets Viwer. If problem still exist, please contact Service Center: https://www.zendesk.com/contact/\n")
                    elif response.status_code==401:
                        print('error '+str(response.status_code)+' Could not authenticate you. Please check your username or password.')
                    elif response.status_code==404:
                        print('error '+str(response.status_code)+' an internal error has occurred.Please restart Tickets Viwer. '+
                              'If problem still exist, please contact Service Center: https://www.zendesk.com/contact/\n')
                    return response.status_code

                    if response.status_code==400:
                        print('Wrong ticket input. Please enter again')
                    elif response.status_code==404:
                        print("Couldn't find the ticket. Please enter again")
                else:
                    break

            # Decode the JSON response into a dictionary and use the data
            data = response.json()
            print('='*33+'Ticket Details'+'='*33)
            print(' Ticket ID:       ',data['ticket']['id'])
            print(' Opener/Requester:',data['ticket']['requester_id'])
            print(' Submitter:       ',data['ticket']['submitter_id'])
            print(' Create time:     ',data['ticket']['created_at'])
            print(' Upgrade Time:    ',data['ticket']['updated_at'])
            print(' Priority:        ',data['ticket']['priority'])
            print(' Subject:         ',data['ticket']['subject'])
            print(' Tickets Tags:    ',data['ticket']['tags'])
            print(' Current Status:  ',data['ticket']['status'])
            print(' Ticket type:     ',data['ticket']['type'])
            print(' Description:\n   ', end='')
            count=0
            for i in range(len(data['ticket']['description'])):
                print(data['ticket']['description'][i], end='')
                if data['ticket']['description'][i]=='\n' and data['ticket']['description'][i+1]!='\n':
                    count=-1
                    print('   ', end='')
                if count%48==45:
                    print('\n ', end='')
                count+=1
            print()
            print('='*80)
            if whetherInput2 is False:
                whetherInput2=True
                dataReturned.append(data)
            else:
                dataReturned[len(dataReturned)-1]=data
        elif inputFromMenu=='quit' or inputFromMenu=='Quit' or inputFromMenu=='q' or inputFromMenu=='Q' or inputFromMenu=='QUIT':
            print("Thanks for using Zendesk Tickets Viewer. Goodbye.")
            break
        else:
            print('The input is not an option. Please try again.')
        print()
    
    return dataReturned

