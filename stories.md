## Generated Story -5128776778721330063
* greet
    - utter_greet
* check_service_withservice{"servicename": "google"}
    - slot{"servicename": "google"}
    - action_checkservice
    - action_checkservice
    - export

## Generated Story -2825798593928793661
* greet
    - utter_greet
* create_JIRA_request
    - action_GetJIRAStatus_param
    - slot{"requested_slot": "JIRAID"}
* inform{"summary": "request?"}
    - slot{"summary": "request?"}
    - action_createJIRArequest_param
    - slot{"summary": "request?"}
    - slot{"requested_slot": "description"}
* inform
    - action_createJIRArequest_param
    - slot{"requested_slot": "description"}
* inform{"summary": "request?"}
    - slot{"summary": "request?"}
    - action_createJIRArequest_param
    - slot{"summary": "request?"}
    - slot{"requested_slot": "description"}
* inform{"summary": "request?"}
    - slot{"summary": "request?"}
    - action_createJIRArequest_param
    - slot{"summary": "request?"}
    - slot{"requested_slot": "description"}
* inform{"environment": "0"}
    - slot{"environment": "0"}
    - export

