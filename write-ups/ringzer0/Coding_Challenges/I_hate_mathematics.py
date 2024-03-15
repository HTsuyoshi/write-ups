import MyTools

def get_equation(page):
	equation = page.text.split('----- BEGIN MESSAGE -----<br />')[1]

	equation = equation.split('<br />')[0]

	decimal = equation.split('+')[0].strip()
	hexa = equation.split('+')[1].split('-')[0].strip()
	bina = equation.split('-')[1].split('=')[0].strip()

	result = int(decimal) + int(hexa, 16) - int(bina, 2)
	return result

flag_start = '<div class="alert alert-info">'
flag_end = '</div>' 
challenge_url = 'https://ringzer0ctf.com/challenges/32'

# Create session
user_session = MyTools.ringzer0_login()

# Go to challenge page
challenge_page = MyTools.challenge_page(user_session, challenge_url)

# Get and do the equation
result = str(get_equation(challenge_page))

# Go to the Flag page
flag_page = MyTools.flag_page(user_session, challenge_url, result)

# Get the flag
flag = MyTools.get_content(flag_start, flag_end, flag_page.text)

# Print flag
MyTools.print_flag(flag)
