import hashlib, MyTools

challenge_url = 'https://ringzer0ctf.com/challenges/13' 
message_start = '----- BEGIN MESSAGE -----<br />'
message_end ='<br'
flag_start = '<div class="alert alert-info">'
flag_end = '</div>'

# Create session
user_session = MyTools.ringzer0_login()

# Go to challenge page
challenge_page = MyTools.challenge_page(user_session ,challenge_url)

# Get the message
hash_code = MyTools.get_content(message_start, message_end, challenge_page.text)

# Hash the message
sha_512 = hashlib.sha512(hash_code.encode('utf-8')).hexdigest()

# Go to the Flag page
flag_page = MyTools.flag_page(user_session, challenge_url, sha_512)

# Split the flag
flag = MyTools.get_content(flag_start, flag_end, flag_page.text)

MyTools.print_flag(flag)
