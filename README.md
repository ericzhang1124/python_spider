# python_spider
python 爬虫小程序，从慕课网学习到的，在此保存


##    程序由4部分构成
###   调度器
###   URL管理器

	管理待抓取URL集合和已抓取URL集合--防止重复和循环抓取

	实现方式：
	1.存储在内存当中使用set结构 (我们用这个实现)
		待爬取URL：set()
		已爬取URL：set()
	2.存储到数据库
		create table urls (url varchar(60) , is_crawled tinyint unsigned);
	3.存储到缓存数据库(redis)
		待爬取URL集合：SET
		已爬取URL集合：SET


###   下载器
###   解析器
