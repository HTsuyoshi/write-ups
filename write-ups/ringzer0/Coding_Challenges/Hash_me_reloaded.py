import hashlib, MyTools

def bin2ascii(bina):
	text = ''
	n = int(bina, 2 )
	return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

def sha512(text):
	return hashlib.sha512(text.encode(encoding='UTF-8')).hexdigest()

message_start = '----- BEGIN MESSAGE -----<br />'
message_end = '<br />'
flag_start = '<div class="alert alert-info">'
flag_end = '</div>'
challenge_url = 'https://ringzer0ctf.com/challenges/14'


# Create a session
user_session = MyTools.ringzer0_login()

# Go to chalenge page
challenge_page = MyTools.challenge_page(user_session, challenge_url)

# Get the bin text
bina = MyTools.get_content(message_start, message_end, challenge_page.text)

# Transform bin to ascii
text = bin2ascii(bina)

# Hash the text
text_hash = sha512(text)

# Go to flag page
flag_page = MyTools.flag_page(user_session, challenge_url, text_hash)

# Get the flag
flag = MyTools.get_content(flag_start, flag_end, flag_page.text)


MyTools.print_flag(flag)
