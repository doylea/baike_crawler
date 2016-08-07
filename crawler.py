import url_manager
import html_downloader
import html_parser
import htmloutputer
import argparse


class crawler(object):
	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = htmloutputer.HtmlOutputer()


	def crawl(self,root_url):
		count = 1
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			try:
				new_url = self.urls.get_new_url()
				print 'crawl %d : %s' %(count,new_url)
				html_cont = self.downloader.download(new_url)
				new_urls,new_data = self.parser.parse(new_url,html_cont)
				self.urls.add_new_urls(new_urls)
				self.outputer.collect_data(new_data)
				if count == 5:
					break
				count = count+1
			except:
				print 'failed'


		self.outputer.output_html()




if __name__=="__main__":
	parser = argparse.ArgumentParser(description='type URL')
	parser.add_argument('-u','--root_url',help='Enter a URL')
	args = parser.parse_args()
	obj_crawl = crawler()
	obj_crawl.crawl(args.root_url)




