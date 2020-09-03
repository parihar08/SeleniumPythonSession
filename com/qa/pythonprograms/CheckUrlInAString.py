# str = "I'm blogger at http://www.pavantestingtools.com/"
# str = "My Profile: https://www.pavantestingtools.com/about.html"
# str = "My Profile: https://www.pavantestingtools.com/about.html" \
#       " and MyBlog:http://www.pavantestingtools.com/"

import re
str1 = "I'm blogger at http://www.pavantestingtools.com/"
str2 = "My Profile: https://www.pavantestingtools.com/about.html" \
       " and MyBlog:http://www.pavantestingtools.com/"

#http://urlregex.com
regexp = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
url1 = re.findall(regexp,str1)
print(url1)

url2 = re.findall(regexp,str2)
print(url2)