## greet
* greet
    - utter_greet
	- action_chat_restart

## thank
* thank
    - utter_thank
	- action_chat_restart

## bye
* bye
    - utter_bye
	- action_chat_restart










## trigger_jenkinsjob
* trigger_jenkinsjob
	- action_jenkins
	- slot{"requested_slot": "jenkinsjob"}
* inform{"jenkinsjob": "sampleapp_ppl"}
	- action_jenkins
	- slot{"jenkinsjob": "sampleapp_ppl"}
	- action_chat_restart
	





	



	


## trigger_deploy1
* trigger_deploy
	- action_jenkins_param
	- slot{"requested_slot": "appname"}
* inform{"appname": "sampleapp"}
	- action_jenkins_param
	- slot{"appname": "sampleapp"}
	- slot{"requested_slot": "environment"}
* env_inform{"environment": "uat"}
	- action_jenkins_param
	- slot{"appname": "sampleapp"}
	- slot{"environment": "uat"}
	- action_chat_restart

## trigger_deploy2
* trigger_deploy
	- action_jenkins_param
	- slot{"requested_slot": "appname"}
* inform{"appname": "sampleapp"}
	- action_jenkins_param
	- slot{"appname": "sampleapp"}
	- slot{"requested_slot": "environment"}
* env_inform{"environment": "dev"}
	- action_jenkins_param
	- slot{"appname": "sampleapp"}
	- slot{"environment": "dev"}
	- action_chat_restart


	


## trigger deploy4
* trigger_deploy{"appname": "sampleapp","environment": "uat"}
	- action_jenkins_param
	- action_chat_restart

## trigger deploy5
* trigger_deploy{"appname": "sampleapp","environment": "prod"}
	- action_jenkins_param
	- action_chat_restart



	



## check_status_withID1
* check_JIRA_Status
    - action_GetJIRAStatus_param
	- slot{"requested_slot": "JIRAID"}
* inform{"JIRAID": "TS-3"}
	- action_GetJIRAStatus_param
	- slot{"JIRAID": "TS-3"}
	- action_chat_restart
	
	
## check_jira_request1
* greet
    - utter_greet
* check_JIRA_Status
    - action_GetJIRAStatus_param
	- slot{"requested_slot": "JIRAID"}
* inform{"JIRAID": "TS-3"}
	- action_GetJIRAStatus_param
	- slot{"JIRAID": "TS-3"}
	- action_chat_restart
	

	







## create JIRA ISSUE31
* create_JIRA_request
	- action_createJIRArequest_param
	- slot{"requested_slot": "summary"}
* inform{"summary": "application not working"}
	- action_createJIRArequest_param
	- slot{"summary": "application not working"}
	- slot{"requested_slot": "description"}
* inform{"description": "page not found for sampleapp.com"}
	- action_createJIRArequest_param
	- slot{"summary": "application not working"}
	- slot{"description": "page not found for sampleapp.com"}
	- slot{"requested_slot": "priority"}
* inform{"priority": "High"}
	- action_createJIRArequest_param
	- slot{"summary": "application not working"}
	- slot{"description": "page not found for sampleapp.com"}	
	- slot{"priority": "High"}
	- action_chat_restart









		
## CHECK SERVICE12
* check_service
	- action_checkservice
	- slot{"requested_slot": "servicename"}
* inform{"servicename": "google"}
	- action_checkservice
	- slot{"servicename": "google"}
	- action_chat_restart

## CHECK SERVICE
* check_service
	- action_checkservice
	- slot{"requested_slot": "servicename"}
* inform{"servicename": "accenture"}
	- action_checkservice
	- slot{"servicename": "accenture"}
	- action_chat_restart

## CHECK SERVICE3
* check_service
	- action_checkservice
	- slot{"requested_slot": "servicename"}
* inform{"servicename": "cnbc"}
	- action_checkservice
	- slot{"servicename": "cnbc"}
	- action_chat_restart
	
## CHECK SERVICE4
* check_service
	- action_checkservice
	- slot{"requested_slot": "servicename"}
* inform{"servicename": "travelers"}
	- action_checkservice
	- slot{"servicename": "travelers"}
	- action_chat_restart

## CHECK SERVICE5
* check_service
	- action_checkservice
	- slot{"requested_slot": "servicename"}
* inform{"servicename": "yahoo"}
	- action_checkservice
	- slot{"servicename": "yahoo"}
	- action_chat_restart
	
	
## CHECK SERVICE6
* check_service{"servicename": "google"}
	- action_checkservice
	- action_chat_restart


 