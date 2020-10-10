import facebook
import requests
from bs4 import BeautifulSoup
from time import sleep

# FUCK FACEBOOK API LIMIT SO I SCRAPPED THAT PAGE
def jdesignerLatest():
	header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	url = 'https://www.facebook.com/juvedesigner/'
	source = requests.get(url ,headers=header).text
	soup = BeautifulSoup(source,'lxml')
	find_post = soup.find('div',class_='_2pie _14i5 _1qkq _1qkx')
	find_dii = find_post.find('div',class_='_5va1 _427x')
	find_form = find_dii.find('form')
	find_input = find_form.findAll('input')
	idd = find_input[2]['value']
	url = 'https://www.facebook.com/208691713357134/posts/{}'.format(idd)
	return idd,url

# FACEBOOK SHARE LINK
def sharePost(url):
	jrc_page_access = ""
	jrc_page_id = ""
	graph = facebook.GraphAPI(jrc_page_access)
	graph.put_object(jrc_page_id,connection_name="feed",message = '',link=url)
	print('done')

post_id = ['653900092169625']

# SLEEP ONE HOURS
SLEEP_TIME = 3600


print('--BOT STARTED--')

while True:
	# GET POST ID AND URL
	idd,url = jdesignerLatest()
	# CHECK ID ALREADY EXIST OR NOT
	if(idd not in post_id):
		try:
			# SHARE JUVEDESIGNER LATEST POST TO JRC
			sharePost(url)
			# ADD POST ID
			post_id.append(idd)
			# SLEEP FOR 1 HR
			sleep(SLEEP_TIME)
		except:
			print('ERROR')
			sleep(SLEEP_TIME)
	else:
		print('POST ALREADY EXIST')
		sleep(SLEEP_TIME)