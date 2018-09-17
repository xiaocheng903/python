from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from scrapy.cmdline import execute

def tick():
	execute(['scrapy','crawl','BTC'])

if __name__=='__main__':
	scheduler=BlockingScheduler()
	scheduler.daemonic=False
	scheduler.add_job(tick,'cron',second=1)
	try:
		scheduler.start()
	except (KeyboardInterrupt,SystemExit):
		scheduler.shutdowm()

