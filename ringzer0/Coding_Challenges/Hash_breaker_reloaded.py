import MyTools, hashlib

def SHA1_salted_breaker (hash, salt):
	for x in range(9999):
		hbreak = str(x) + salt
		if hashlib.sha1(hbreak.encode(encoding='UTF-8')).hexdigest() == hash:
			return str(x)
			
challenge_url = 'https://ringzer0ctf.com/challenges/57'
flag_start = '<div class="alert alert-info">'
flag_end = '</div>'
hash_start = "----- BEGIN HASH -----<br />"
hash_end = "<br />"
salt_start = "----- BEGIN SALT -----<br />" 
salt_end = "<br />"

# Create session
user_session = MyTools.ringzer0_login()

# Go to challenge page
challenge_page = MyTools.challenge_page(user_session, challenge_url)

# Get the hash
hash = MyTools.get_content(hash_start, hash_end, challenge_page.text)

# Get the salt
salt = MyTools.get_content(salt_start, salt_end, challenge_page.text)

# Break the hash
broken_hash = SHA1_salted_breaker (hash, salt)

# Go to the challenge page
flag_page = MyTools.flag_page(user_session, challenge_url, broken_hash)

# Split the flag
flag = MyTools.get_content(flag_start, flag_end, flag_page.text)

MyTools.print_flag(flag)

