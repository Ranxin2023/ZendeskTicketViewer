# Zendesk Ticket Viewer
## Introduction 
  Zendesk Ticket Viewer is a tool to view the ticket list and individual ticket detail.

## Installation

1. Python Platform Installation
     Zendesk Ticket Viewer package is python based source code package. So you have to install below software platform. 
     python 3.0 or newer. Suggest choose v3.8 (security Status). download weblink:  https://www.python.org/downloads/ 
2. Python Requests Library Installation
     Release v2.26.0. download weblink : https://docs.python-requests.org/en/latest/ 

3. Zendesk Ticket Viewer Installation
     Unzip ztview.zip in your working direction.

## Run
1. Run Zendesk Ticket Viewer in normal mode
  - Enter console window and go to your working direction.  Enter python3 ztViewer.py
  - input username and password  (Username: rstli@ucdavis.edu    passsword: R@ndyli94041424)
  - choose 1 or 2 on menu.

2. Run Zendesk Ticket Viewer in Unit Test mode
  step 1: double click Python 3.8 (64-bit) icon enter python console . Enter:  python3 ztview_unittest
  step 2: Test 
     case 1 : mistake username   error 401 
     case 2 : mistake password   error 401 
	 case 3 : input 1,2 in menu                 normal exit
	 case 4 : input quit,QUIT,Quit,Q,q in menu  normal exit
	 case 5 : input number like 3,4 except 1 and 2    reinput
	 case 6 : input number exceed scope of ticket number after input 2   error 400  reinput

  * Notification: Developer choose Python unittest test Framework. Unitest is included in python package. No need install. 
  
## Project structure
```sh
  TICKET_PROJECT/
│
├── RanxinLiZViewer/                       # Main source code folder
│   ├── ztViewer.py                        # Core script to view Zendesk tickets
│   ├── ztViewerDebug.py                   # Debugging script for ticket viewer
│   ├── ztViewerDebugUnittest.py           # Unit test script for ztViewer
│   ├── Account.txt                        # Developer's Zendesk account credentials
│   ├── README.txt                         # Basic installation and usage instructions
│   └── __pycache__/                       # Compiled Python files (automatically generated)
│
├── static/                                # Static assets for the application
│   ├── css/                               # CSS stylesheets
│       └── form_styles.css                # Stylesheet for ticket form
│
├── views/                                 # Views and templates
│   └── ticket_form.tpl                    # HTML template for ticket forms
│
├── tickets.json                           # JSON file containing ticket data (example)
├── app.py                                 # Application entry point for running the project
├── get_all.py                             # Script to fetch all Zendesk tickets
├── get_groups.py                          # Script to fetch ticket groups
├── put_comment.py                         # Script to add comments to tickets
├── command.txt                            # Instructions or sample commands for testing
├── temporary.txt                          # Temporary notes or data files
├── .gitignore                             # Git ignore file to exclude unnecessary files
└── README.md                              # Project documentation and instructions

```

## Appendix
Appendix A: Package files list
  ztview.py               Zendesk Ticket Viewer source code besed on python
  ztview_unittest.py      unit test source code besed on python 
  README.txt              this file installation and installation and usage instructions
  Account.txt             developer's account in Zendesk

Appendix B: Zendesk account information 
  1- Rigister account:     			https://www.zendesk.com/register#getstarted
  2- Developer's account:   		Username: rstli@ucdavis.edu    passsword: R@ndyli94041424
  3- Developer's subdomain:			https://zcczendeskcodingchallenge8643.zendesk.com
  4- Developer's API token:			hLWJTPCI6vXxIFjGcT6XnxDpG7MnfVSehNy7RZLP
  
Appendix C: Curl Tools
  Zendesk REST API docs use cURL as tools. This is not necessary for normal user. 
  Curl tools ABC : https://developer.zendesk.com/documentation/developer-tools/getting-started/installing-and-using-curl/ 
  curl software download: https://curl.se/download.html
  Installing cURL in windows10: https://developer.zendesk.com/documentation/developer-tools/getting-started/installing-and-using-curl/#windows-10-version-1803-or-later
  Setting cURL in Windows10: https://developer.zendesk.com/documentation/developer-tools/getting-started/installing-and-using-curl/#using-curl-in-windows
