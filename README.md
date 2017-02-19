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


###   网页下载器
	
	将互联网上的URL对应的网页下载到本地工具

	实现方式：
	1.使用urllib2
	2.使用requests(我们用这个)


###   解析器

	从网页中提取有价值数据的工具

	实现方式：
	获取到网页字符串，进行解析，从中获取到有价值的数据和新URL列表

	Python支持的几个解析器：
	a. 正则表达式
	b. html.parser
	c. Beautiful Soup （我们用这个，他支持html.parser&&Ixml）
	d. Ixml

	BeautifulSoup原理简介
	a.获取到html网页
	b.使用网页创建一个BeautifulSoup对象
	c.利用该对象的find、find_all搜索节点
	d.访问节点的名称、属性、文本
	eg.
		<a herf='123.html' class='article_link'>Python</a>
		节点名称：a
		节点属性：herf='123.html' class='article_link'
		节点文本：Python

	Create a BeautifulSoup Object
	soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
	// html_doc:html文档字符串
	// html.parser:html解析器
	// from_encoding:HTML文档的编码，需要查看网页


## 分析爬虫目标

	目标：百度百科Python词条相关词条网页 - 标题和简介
	入口页：http://baike.baidu.com/item/Python
	URL格式: /view/123231.htm
	数据格式:
		标题:<dd class="lemmaWge-lemmaTitle-title"><h1>***</h1></dd>
		简介:<div class="lemma-summary">***<div>
	页面编码:UTF-8
	




