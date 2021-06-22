
from rethinkdb import RethinkDB
r = RethinkDB()
r.connect( "localhost", 28015).repl()
r.db("test").table_create("newsletters").run()

