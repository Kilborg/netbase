import requests
import json
import urllib

base_url = 'https://api.netbase.com:443/cb/insight-api/2/'
#authentication
user_name = 'matthew.butner@rga.com'
password = 'rg@12345'

class TopicThemeIDExtractor(object):

	def __init__(self, topic_name):
		self.topic_name = topic_name

	def get_topic_id(self):
		topic_id_url = base_url + 'topics?scope=USER'
		data = [{u'version': u'CB2', u'languageFilters': [u'English'], u'facebookPage': None, u'channelId': None, u'userId': u'10007', u'brandsCount': u'5', u'owner': {u'accountProfileId': u'1183', u'id': u'10007', u'name': u'Matthew Butner'}, u'includedDomainsCount': u'0', u'downloadProgressPercentage': 0, u'createDate': u'2013-05-07 18:59:29', u'fhTwitterHistoryEndDate': None, u'excludedDomainsCount': u'0', u'downloadRemainingDays': 0, u'includedAuthorsCount': u'0', u'excludedTermsCount': u'0', u'mainBrand': None, u'topicId': u'172731', u'sharing': u'PUBLIC', u'contentType': u'SocialWeb', u'description': u'', u'tags': [u'PROVIDE'], u'fhTwitterStatus': u'OFF', u'twitterHandle': None, u'fhTwitterStartDate': None, u'includedTermsCount': u'0', u'name': u'livestrong', u'updateDate': u'2013-05-07 19:05:32', u'fhTwitterHistoryStartDate': None, u'excludedAuthorsCount': u'0'}, {u'version': u'CB2', u'languageFilters': [u'English'], u'facebookPage': None, u'channelId': None, u'userId': u'10007', u'brandsCount': u'4', u'owner': {u'accountProfileId': u'1183', u'id': u'10007', u'name': u'Matthew Butner'}, u'includedDomainsCount': u'0', u'downloadProgressPercentage': 0, u'createDate': u'2013-05-07 17:39:57', u'fhTwitterHistoryEndDate': None, u'excludedDomainsCount': u'0', u'downloadRemainingDays': 0, u'includedAuthorsCount': u'0', u'excludedTermsCount': u'0',u'mainBrand': None, u'topicId': u'172679', u'sharing': u'PUBLIC', u'contentType': u'SocialWeb', u'description': u'', u'tags': [u'PROVIDE'], u'fhTwitterStatus':u'OFF', u'twitterHandle': None, u'fhTwitterStartDate': None, u'includedTermsCount': u'0', u'name': u'Gifts.com', u'updateDate': u'2013-05-07 17:39:57', u'fhTwitterHistoryStartDate': None, u'excludedAuthorsCount': u'0'}, {u'version': u'CB2', u'languageFilters': [u'English'], u'facebookPage': None, u'channelId': None, u'userId': u'10007', u'brandsCount': u'11', u'owner': {u'accountProfileId': u'1183', u'id': u'10007', u'name': u'Matthew Butner'}, u'includedDomainsCount': u'0', u'downloadProgressPercentage': 0, u'createDate': u'2013-05-08 00:31:05', u'fhTwitterHistoryEndDate': None, u'excludedDomainsCount': u'0', u'downloadRemainingDays': 0, u'includedAuthorsCount': u'0', u'excludedTermsCount': u'0', u'mainBrand': None, u'topicId': u'172883', u'sharing': u'PUBLIC', u'contentType': u'SocialWeb', u'description': u'', u'tags': [u'MICROSOFT'], u'fhTwitterStatus': u'OFF', u'twitterHandle': None, u'fhTwitterStartDate': None, u'includedTermsCount': u'0',u'name': u'iPad 3rd generation', u'updateDate': u'2013-05-08 18:49:21', u'fhTwitterHistoryStartDate': None, u'excludedAuthorsCount': u'0'}, {u'version': u'CB2',u'languageFilters': [u'English'], u'facebookPage': None, u'channelId': None, u'userId': u'10007', u'brandsCount': u'11', u'owner': {u'accountProfileId': u'1183', u'id': u'10007', u'name': u'Matthew Butner'}, u'includedDomainsCount': u'0',u'downloadProgressPercentage': 0, u'createDate': u'2013-05-08 00:37:01', u'fhTwitterHistoryEndDate': None, u'excludedDomainsCount': u'0', u'downloadRemainingDays': 0, u'includedAuthorsCount': u'0', u'excludedTermsCount': u'0', u'mainBrand':None, u'topicId': u'172887', u'sharing': u'PUBLIC', u'contentType': u'SocialWeb', u'description': u'', u'tags': [u'MICROSOFT'], u'fhTwitterStatus': u'OFF', u'twitterHandle': None, u'fhTwitterStartDate': None, u'includedTermsCount': u'0', u'name': u'iPad 4th generation', u'updateDate': u'2013-05-08 18:54:40', u'fhTwitterHistoryStartDate': None, u'excludedAuthorsCount': u'0'}, {u'version': u'CB2',u'languageFilters': [u'English'], u'facebookPage': None, u'channelId': None, u'userId': u'10007', u'brandsCount': u'3', u'owner': {u'accountProfileId': u'1183', u'id': u'10007', u'name': u'Matthew Butner'}, u'includedDomainsCount': u'0', u'downloadProgressPercentage': 0, u'createDate': u'2013-05-08 00:20:37', u'fhTwitterHistoryEndDate': None, u'excludedDomainsCount': u'0', u'downloadRemainingDays': 0, u'includedAuthorsCount': u'0', u'excludedTermsCount': u'0', u'mainBrand': None, u'topicId': u'172875', u'sharing': u'PUBLIC', u'contentType': u'SocialWeb', u'description': u'', u'tags': [u'MICROSOFT'], u'fhTwitterStatus': u'OFF', u'twitterHandle': None, u'fhTwitterStartDate': None, u'includedTermsCount': u'0', u'name': u'iPad mini ', u'updateDate': u'2013-05-08 00:26:57', u'fhTwitterHistoryStartDate': None, u'excludedAuthorsCount': u'0'}]
		for i in data:
			if i['name'] == self.topic_name:
				topic_id = i['topicId']
				return topic_id

	def get_topic_theme_dict(self):
		theme_id_url = base_url + 'themes?scope=USER&categories=' + self.topic_name
		themedata = [{u'sharing': u'PUBLIC', u'name': u'Emotional support ', u'tags': [u'LIVESTRONG'], u'editedDate': u'2013-05-06 18:02:19', u'themeId': u'17487', u'userId': u'10007', u'createdDate': u'2013-04-29 19:22:27', u'owner': {u'accountProfileId': u'1183', u'id': u'10007', u'name': u'Matthew Butner'}}, {u'sharing': u'PUBLIC', u'name': u'Infertility ', u'tags': [u'LIVESTRONG'], u'editedDate': u'2013-05-06 18:01:22', u'themeId': u'16687', u'userId': u'10007', u'createdDate': u'2013-04-2107:43:11', u'owner': {u'accountProfileId': u'1183', u'id': u'10007', u'name': u'Matthew Butner'}}, {u'sharing': u'PUBLIC', u'name': u'Insurance ', u'tags': [u'LIVESTRONG'], u'editedDate': u'2013-05-06 18:00:37', u'themeId': u'17277', u'userId': u'10007', u'createdDate': u'2013-04-26 21:03:17', u'owner': {u'accountProfileId': u'1183', u'id': u'10007', u'name': u'Matthew Butner'}}, {u'sharing': u'PUBLIC', u'name': u'LIVESTRONG Day ', u'tags': [u'LIVESTRONG'], u'editedDate': u'2013-05-06 17:59:12', u'themeId': u'17593', u'userId': u'10007', u'createdDate':u'2013-04-30 18:56:41', u'owner': {u'accountProfileId': u'1183', u'id': u'10007', u'name': u'Matthew Butner'}}, {u'sharing': u'PUBLIC', u'name': u'LIVESTRONG Navigation', u'tags': [u'LIVESTRONG'], u'editedDate': u'2013-05-06 17:58:57', u'themeId': u'17515', u'userId': u'10007', u'createdDate': u'2013-04-29 21:16:38', u'owner': {u'accountProfileId': u'1183', u'id': u'10007', u'name': u'Matthew Butner'}}, {u'sharing': u'PUBLIC', u'name': u'Transportation Services', u'tags': [u'LIVESTRONG'], u'editedDate': u'2013-05-06 17:58:03', u'themeId': u'17211', u'userId': u'10007', u'createdDate': u'2013-04-25 20:22:33', u'owner': {u'accountProfileId': u'1183', u'id': u'10007', u'name': u'Matthew Butner'}}, {u'sharing': u'PUBLIC', u'name': u'Treatment concerns', u'tags': [u'LIVESTRONG'], u'editedDate': u'2013-05-06 17:57:40', u'themeId': u'17491', u'userId': u'10007', u'createdDate': u'2013-04-29 19:43:17', u'owner': {u'accountProfileId': u'1183', u'id': u'10007', u'name': u'Matthew Butner'}}]
		themes = {}
		for z in themedata:
			k = z['name']
			p = z['themeId']
			themes[k] = p
		return themes

def main():
	#***** ENTER TERM BELOW *****
	topic_name = 'livestrong'
	ponestrong = TopicThemeIDExtractor(topic_name)
	print ponestrong.get_topic_id()
	print ponestrong.get_topic_theme_dict()

if __name__ == '__main__':
	main()



	
 

