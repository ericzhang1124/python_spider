# coding:utf-8

'输出器'


class HtmlOutputer(object):
	def __init__(self):
		self.datas = []

	def collect_data(self, data):
		if data is None:
			return 
		self.datas.append(data)

	def output_html(self):

		with open('output.html', 'w') as font:
			font.write("<html>")
			font.write("<head>")
			font.write('''<meta charset="UTF-8">''')
			font.write("</head>")
			font.write("<body>")
			font.write("<table>")
			for data in self.datas:
				font.write("<tr>")
				font.write("<td>%s</td>" % data['url'])
				font.write("<td>%s</td>" % data['title'].encode('utf-8'))
				font.write("<td>%s</td>" % data['summary'].encode('utf-8'))
				font.write("</tr>")
			font.write("</table>")
			font.write("</body>")
			font.write("</html>")