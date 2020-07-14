from Downloader import mangadex

downloader = mangadex.Mangadex(path='F:\selenium\chromedriver.exe')
downloader.login(username='guest123qwe', password='guest123qwe')
path = downloader.createFolder('F:\manga')

# Exemple 1
# Download the single chapter
number = downloader.numberPages(link='https://mangadex.org/chapter/559372/1')
downloader.downloadSelectedChapter(items=number, path=path)
downloader.quit()
