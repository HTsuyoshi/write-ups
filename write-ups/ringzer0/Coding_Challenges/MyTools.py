import requests, getpass

# Create a session to keep logged-in
def ringzer0_login():
	
	url = 'https://ringzer0ctf.com/login'
	user = input('Username: ').strip()
	passwd = getpass.getpass().strip()
	print()

	login = {'username': user,
			'password': passwd}
	
	user_session = requests.Session()
	user_session.post(url, login)
	
	return user_session

# Go to the challenge page
def challenge_page(user_session, challenge_url):
		
	challenge_page = user_session.get(challenge_url)

	# Assert the page
	try:
		assert challenge_page.url == challenge_url
	except AssertionError as e:
		e.args = ('Username or password is invalid', ':/', 'you went to:', challenge_page.url)
		raise	
	
	print('-'*60)
	print('Sussesful logged in ' + challenge_page.url)
	print('-'*60)
	print()

	return challenge_page

# Go to the flag page
def flag_page(user_session, challenge_url, final_url):

	flag_url = challenge_url + '/' + final_url
	flag_page = user_session.get(flag_url)
	
	# Assert the page
	try:
		assert flag_page.url == flag_url
	except AssertionError as e:
		e.args = ('final_url went wrong', ':/')
		raise

	print('-'*60)
	print('Sussesful entered in  ' + flag_page.url)
	print('-'*60)
	print()

	return flag_page

# Split
def get_content(start, end, message):
	
	content = message.split(start)[1].strip()
	content = content.split(end)[0].strip()
	
	return content 

def print_flag(flag):
	
	print('*'*60)
	print(flag)
	print('*'*60)
