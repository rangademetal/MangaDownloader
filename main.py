from Downloader import nhentai as manga
from Downloader import mangadex
# downloader = manga.Downloader(path = '/usr/local/bin/chromedriver')
# downloader.getPage()
# downloader.randomStory()
# downloader.getImage()

downloader = mangadex.Mangadex(path = '/usr/local/bin/chromedriver')
downloader.getPageMangadex()
downloader.login()
downloader.search(manga='Devil May Cry 5 -Visions of V-')
downloader.download(path='/Users/andreistroe/Pictures')