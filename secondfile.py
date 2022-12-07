# This is the second file
import secrets
import string


_names = []
for i in range(0,30):
    _string=""
    _string=''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for k in range(10))
    _names.append(_string)
    print(_names[i])

#end