pytempmail Copyright matthewrobertbell@gmail.com 2010. GPL v2.

redis - http://code.google.com/p/redis/
bottle - http://bottle.paws.de/

pytempmail is pretty much a clone of mailinator. redismail.py acts as the mail server, bottlemail.py serves out json for individual mailboxes, or a 404 if no recent messages.

You need to be running redis somewhere for this, preferably on localhost.
redismail.py will need to be run as root if you want to accept mail on port 25.

the copying all elements in a mailbox list out of and back into redis is to get around a redis EXPIRE limitation.
