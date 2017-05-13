#imports

# import sqls
import sqlite3


#sql events
conn=sqlite3.connect("database")
c=conn.cursor()
#----------------------------------------------------------

class Profile(object):
	def __init__(self,userid):
		self.userid = userid
	
	def on_register(self):
		try:
			user=c.execute("SELECT * FROM profile WHERE Id = '"+self.userid+"'")
			user.fetchone()[1]==self.userid
			return True
		except:
			user = c.execute("INSERT INTO profile (Id) VALUES ({0})".format(self.userid))
			conn.commit()
			return False
	def have_eggs(self):
		c.execute("SELECT eggs FROM profile WHERE Id='{0}'".format(self.userid))
		eggs=c.fetchone()[0]
		return eggs
	def have_experience(self):
		c.execute("SELECT experience FROM profile WHERE Id='{0}'".format(self.userid))
		experience = c.fetchone()[0]
		return experience
	def set_title(self,title:str):
		c.execute("UPDATE profile set title = '{0}' WHERE Id = '{1}'".format(title,self.userid))
		conn.commit()
		return True
	def set_bio(self,bio:str):
		c.execute("UPDATE profile set bio = '{0}' WHERE Id = '{1}'".format(bio,self.userid))
		conn.commit()
		return True
	def get_experience(self,exp:int):
		c.execute("UPDATE profile set experience = experience + {0}  WHERE Id = '{1}'".format(exp,self.userid))
		conn.commit()
		return True
	def get_eggs(self,exp:int):
		c.execute("UPDATE profile set eggs = eggs + {0}  WHERE Id = '{1}'".format(exp,self.userid))
		conn.commit()
		return True
	def profiler(self):
		user=c.execute("SELECT * FROM Profile WHERE Id = '{0}'".format(self.userid))
		profile = c.fetchone()
		return profile
		


