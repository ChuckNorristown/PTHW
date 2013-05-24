import web

web.config.debug = False

urls = (
	"/count", "count",
	"/reset", "reset"
)
app = web.application(urls, locals())
store = web.sessionsDiskStore('sessions')
sessions = web.sessions.Sessions(app, store, initializer={'count': 0})

class count:
	def GET(self):
		session.count += 1
		return str(session.count)

class reset:
	def GET(self):
		session.kill()
		return ""

if __name__ == "__main__":
	app.run()