import hashlib, MyTools

def Hash_breaker_SHA1_4(hash_to_break):
	for x in range(9999):
		if hashlib.sha1(str(x).encode(encoding='UTF-8')).hexdigest() == hash_to_break:
			return x

# In this challenge I found that the hash is a 4 digits number and the hash is SHA1

challenge_url = 'https://ringzer0ctf.com/challenges/56'
message_start = '----- BEGIN HASH -----<br />'
message_end = '<br'
flag_start = '<div class="alert alert-info">'
flag_end = '</div>'

# Create session
user_session = MyTools.ringzer0_login()

# Go to challenge page
challenge_page = MyTools.challenge_page(user_session, challenge_url)

# Get the message
hash_to_break = MyTools.get_content(message_start, message_end, challenge_page.text)

# Break the hash
broken_hash = str(Hash_breaker_SHA1_4(hash_to_break))

# Go to the Flag page
flag_page = MyTools.flag_page(user_session, challenge_url, broken_hash)

# Split the flag
flag = MyTools.get_content(flag_start, flag_end, flag_page.text)

MyTools.print_flag(flag)
