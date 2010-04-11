import bottle,redis
R = redis.Redis()
@bottle.route('/mailboxes/:mailbox')
def show_mailbox(mailbox):
	mail = R.lrange(mailbox,0,-1)
	if mail is None:
		bottle.abort(404)
	else:
		return dict(zip(range(len(mail)),mail))
bottle.run(host='localhost', port=9999)
