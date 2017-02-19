# coding:utf-8

class UrlManager(object):

	def __init__(self):
		'''
		初始化两个集合，一个存放未爬取的urls，一个存放已爬取过的urls
		'''
		self.new_urls = set()
		self.old_urls = set()
	
	def add_new_url(self, url):
		'''
		添加一个URL进入 SET new_urls
		'''
		if url is None:
			return
		if url not in self.new_urls and url not in self.old_urls:
			self.new_urls.add(url)	

	def add_new_urls(self, urls):
		'''
		添加url列表进入 SET new_urls
		'''
		if urls is None or len(urls) == 0:
			return 
		for url in urls:
			self.add_new_url(url)

	def has_new_url(self):
		'''
		判断 SET new_url 是否为空
		'''
		return len(self.new_urls) != 0

	def get_new_url(self):
		'''
		从SET new_urls 获取一个url,使用后将其从列表移除并添加到SET old_urls里
		'''
		new_url = self.new_urls.pop() # pop()移除并返回移除对象
		self.old_urls.add(new_url)
		return new_url


	
