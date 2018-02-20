# module of cube upgrade record

import sqlite3

class upgraderecord(object):
	def __init__(self, recordfile):
		self.recordfile = recordfile
		self.conn = sqlite3.connect(self.recordfile)
		self.cursor = self.conn.cursor()
		self.cursor.execute('create table if not exists upgradelist (ip varchar(20) primary key, isupgraded varchar(3), upgradetime varchar (30))')
		
		

	def update(self, ip, isupgraded, time):
		sql = 'update upgradelist set isupgraded=\'' + isupgraded +   '\' , upgradetime=\'' + time + '\' where ip= \'' + ip + '\''
		print sql
		self.cursor.execute(sql)
		if self.cursor.rowcount == 1:
			self.conn.commit()
			return 0
		else:
			return -1
		
		
	def find(self, ip):
		sql = 'select * from upgradelist where ip=\'' + ip + '\''
		self.cursor.execute(sql)
		record = self.cursor.fetchone()
		print record
		
		if record[0] == ip and record[1] == 'no':
			print('found the record of', ip, 'wasn\'t upgraded')
			return 0
		elif record[0] == ip and record[1] == 'yes':
			print('found the reocrd of', ip, 'was upgraded')
			return 1
		else:
			print('can\'t found the record of', ip)
			return -1
			
		
	
	def insert(self, ip, isupgrade, time):
		sql = 'insert into upgradelist values (\'' + ip + '\', \'' + isupgrade + '\', \'' + time + '\')'
		print sql
		self.cursor.execute(sql)
		rowcount = self.cursor.rowcount
		
		if rowcount == 1:
			self.conn.commit()
			return 0
		else:
			return -1
			
			
	def close(self):
		self.conn.close()
		
def main():
	upgradetask = upgraderecord('test.db')
	ip = '192.168.1.2'
	isfind = upgradetask.find(ip)
	
	if isfind == 1:
		print 'update table to no'
		upgradetask.update(ip, 'no', '2018')
	else:
		print 'update table to yes'
		upgradetask.update(ip, 'yes', '2018')
		
	upgradetask.insert('192.168.1.3', 'no', '2017')
		
	upgradetask.close()

if __name__ == '__main__':
	main()