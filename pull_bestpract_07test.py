import requests
import json
import urllib

base_url = 'https://api.netbase.com:443/cb/insight-api/2/'
#authentication
user_name = 'matthew.butner@rga.com'
password = 'rg@12345'



#def get_topic_id():
topic_id_url = base_url + 'topics?scope=USER'
topic_id_req = requests.get(topic_id_url, auth=(user_name, password))
topic_id_json = topic_id_req.json()
#data = [{u'version': u'CB2', u'languageFilters': [u'English'], u'facebookPage': None, u'channelId': None, u'userId': u'10007', u'brandsCount': u'5', u'owner': {u'accountProfileId': u'1183', u'id': u'10007', u'name': u'Matthew Butner'}, u'includedDomainsCount': u'0', u'downloadProgressPercentage': 0, u'createDate': u'2013-05-07 18:59:29', u'fhTwitterHistoryEndDate': None, u'excludedDomainsCount': u'0', u'downloadRemainingDays': 0, u'includedAuthorsCount': u'0', u'excludedTermsCount': u'0', u'mainBrand': None, u'topicId': u'172731', u'sharing': u'PUBLIC', u'contentType': u'SocialWeb', u'description': u'', u'tags': [u'PROVIDE'], u'fhTwitterStatus': u'OFF', u'twitterHandle': None, u'fhTwitterStartDate': None, u'includedTermsCount': u'0', u'name': u'livestrong', u'updateDate': u'2013-05-07 19:05:32', u'fhTwitterHistoryStartDate': None, u'excludedAuthorsCount': u'0'}, {u'version': u'CB2', u'languageFilters': [u'English'], u'facebookPage': None, u'channelId': None, u'userId': u'10007', u'brandsCount': u'4', u'owner': {u'accountProfileId': u'1183', u'id': u'10007', u'name': u'Matthew Butner'}, u'includedDomainsCount': u'0', u'downloadProgressPercentage': 0, u'createDate': u'2013-05-07 17:39:57', u'fhTwitterHistoryEndDate': None, u'excludedDomainsCount': u'0', u'downloadRemainingDays': 0, u'includedAuthorsCount': u'0', u'excludedTermsCount': u'0',u'mainBrand': None, u'topicId': u'172679', u'sharing': u'PUBLIC', u'contentType': u'SocialWeb', u'description': u'', u'tags': [u'PROVIDE'], u'fhTwitterStatus':u'OFF', u'twitterHandle': None, u'fhTwitterStartDate': None, u'includedTermsCount': u'0', u'name': u'Gifts.com', u'updateDate': u'2013-05-07 17:39:57', u'fhTwitterHistoryStartDate': None, u'excludedAuthorsCount': u'0'}, {u'version': u'CB2', u'languageFilters': [u'English'], u'facebookPage': None, u'channelId': None, u'userId': u'10007', u'brandsCount': u'11', u'owner': {u'accountProfileId': u'1183', u'id': u'10007', u'name': u'Matthew Butner'}, u'includedDomainsCount': u'0', u'downloadProgressPercentage': 0, u'createDate': u'2013-05-08 00:31:05', u'fhTwitterHistoryEndDate': None, u'excludedDomainsCount': u'0', u'downloadRemainingDays': 0, u'includedAuthorsCount': u'0', u'excludedTermsCount': u'0', u'mainBrand': None, u'topicId': u'172883', u'sharing': u'PUBLIC', u'contentType': u'SocialWeb', u'description': u'', u'tags': [u'MICROSOFT'], u'fhTwitterStatus': u'OFF', u'twitterHandle': None, u'fhTwitterStartDate': None, u'includedTermsCount': u'0',u'name': u'iPad 3rd generation', u'updateDate': u'2013-05-08 18:49:21', u'fhTwitterHistoryStartDate': None, u'excludedAuthorsCount': u'0'}, {u'version': u'CB2',u'languageFilters': [u'English'], u'facebookPage': None, u'channelId': None, u'userId': u'10007', u'brandsCount': u'11', u'owner': {u'accountProfileId': u'1183', u'id': u'10007', u'name': u'Matthew Butner'}, u'includedDomainsCount': u'0',u'downloadProgressPercentage': 0, u'createDate': u'2013-05-08 00:37:01', u'fhTwitterHistoryEndDate': None, u'excludedDomainsCount': u'0', u'downloadRemainingDays': 0, u'includedAuthorsCount': u'0', u'excludedTermsCount': u'0', u'mainBrand':None, u'topicId': u'172887', u'sharing': u'PUBLIC', u'contentType': u'SocialWeb', u'description': u'', u'tags': [u'MICROSOFT'], u'fhTwitterStatus': u'OFF', u'twitterHandle': None, u'fhTwitterStartDate': None, u'includedTermsCount': u'0', u'name': u'iPad 4th generation', u'updateDate': u'2013-05-08 18:54:40', u'fhTwitterHistoryStartDate': None, u'excludedAuthorsCount': u'0'}, {u'version': u'CB2',u'languageFilters': [u'English'], u'facebookPage': None, u'channelId': None, u'userId': u'10007', u'brandsCount': u'3', u'owner': {u'accountProfileId': u'1183', u'id': u'10007', u'name': u'Matthew Butner'}, u'includedDomainsCount': u'0', u'downloadProgressPercentage': 0, u'createDate': u'2013-05-08 00:20:37', u'fhTwitterHistoryEndDate': None, u'excludedDomainsCount': u'0', u'downloadRemainingDays': 0, u'includedAuthorsCount': u'0', u'excludedTermsCount': u'0', u'mainBrand': None, u'topicId': u'172875', u'sharing': u'PUBLIC', u'contentType': u'SocialWeb', u'description': u'', u'tags': [u'MICROSOFT'], u'fhTwitterStatus': u'OFF', u'twitterHandle': None, u'fhTwitterStartDate': None, u'includedTermsCount': u'0', u'name': u'iPad mini ', u'updateDate': u'2013-05-08 00:26:57', u'fhTwitterHistoryStartDate': None, u'excludedAuthorsCount': u'0'}]
print topic_id_json
#for i in topic_id_json:
#	if i['name'] == self.topic_name:
#		topic_id = i['topicId']
#		return topic_id



	
 

