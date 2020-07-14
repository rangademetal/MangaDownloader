from Downloader import mangadex

downloader = mangadex.Mangadex(path='F:\selenium\chromedriver.exe')
downloader.login(username='guest123qwe', password='guest123qwe')
path = downloader.createFolder('F:\manga')

arr = []
downloader.getLink('https://mangadex.org/chapter/559372/1')
n = downloader.numberPagesChapter(items=arr)

downloader.getLink('https://mangadex.org/chapter/559372/1')
downloader.downloadAllPages(arr=n, path=path)
