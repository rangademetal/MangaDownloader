from Downloader import nhentai as manga
from Downloader import mangadex
# downloader = manga.Downloader(path = '/usr/local/bin/chromedriver')
# downloader.getPage()
# downloader.randomStory()
# downloader.getImage()

downloader = mangadex.Mangadex(path ='C:\Program Files (x86)\chromedriver.exe')
downloader.getPageMangadex()
downloader.login()
downloader.search(manga='Devil May Cry 5 -Visions of V-')
downloader.download(path='C:/Users/stroe/Pictures')