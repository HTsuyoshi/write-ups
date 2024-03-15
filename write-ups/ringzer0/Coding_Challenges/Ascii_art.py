import requests
import getpass
import time
import MyTools

# Convert ascii art to char
def convert_message(ascii_art):
	url_message = ''
	message = ascii_art.split('<br /><br />')
	five = 'xxxxx<br />x&nbsp;&nbsp;&nbsp;&nbsp;<br />&nbsp;xxxx<br />&nbsp;&nbsp;&nbsp;&nbsp;x<br />xxxxx<br />'
	read_10_numbers = 0
	for char in message:
		if len(char) > 150:
			separate_char = char.partition(five)
			for subchar in separate_char:
				url_message += letter(subchar)
		else:
			url_message += letter(char)
		read_10_numbers += 1
	return url_message

# Convert ascii char to char
def letter(char):
	number_dict = {'&nbsp;xxx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x<br />x&nbsp;&nbsp;&nbsp;x<br />x&nbsp;&nbsp;&nbsp;x<br />&nbsp;xxx&nbsp;' : '0',
	'&nbsp;xx&nbsp;&nbsp;<br />x&nbsp;x&nbsp;&nbsp;<br />&nbsp;&nbsp;x&nbsp;&nbsp;<br />&nbsp;&nbsp;x&nbsp;&nbsp;<br />xxxxx' : '1', 
	'&nbsp;xxx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x&nbsp;<br />&nbsp;&nbsp;xx&nbsp;<br />&nbsp;x&nbsp;&nbsp;&nbsp;<br />xxxxx' : '2', 
	'&nbsp;x&nbsp;&nbsp;&nbsp;x<br />x&nbsp;&nbsp;&nbsp;&nbsp;x<br />&nbsp;xxxxx<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br />&nbsp;&nbsp;&nbsp;&nbsp;x' : '4', 
	'xxxxx<br />x&nbsp;&nbsp;&nbsp;&nbsp;<br />&nbsp;xxxx<br />&nbsp;&nbsp;&nbsp;&nbsp;x<br />xxxxx<br />' : '5', 
	'xxxxx<br />x&nbsp;&nbsp;&nbsp;&nbsp;<br />&nbsp;xxxx<br />&nbsp;&nbsp;&nbsp;&nbsp;x<br />xxxxx' : '5',
	'&nbsp;xxx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x<br />&nbsp;&nbsp;xx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x<br />&nbsp;xxx&nbsp;' : '3'}
	return number_dict.get(char, '')

challenge_url = 'https://ringzer0ctf.com/challenges/119'
message_start = '----- BEGIN MESSAGE -----<br />'
message_end = '----- END MESSAGE -----<br />'
flag_start = '<div class="flag">'
flag_end = '</div>'

# login
user_session = MyTools.ringzer0_login()
text_challenge_page = MyTools.challenge_page(user_session, challenge_url).text

# get message
ascii_art = MyTools.get_content(message_start, message_end, text_challenge_page)
url_message = convert_message(ascii_art)
flag_page = user_session.get(challenge_url + '/' + url_message.strip())
flag = MyTools.get_content(flag_start, flag_end, flag_page.text)
print(flag)
