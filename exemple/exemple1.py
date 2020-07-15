from Downloader import mangadex

downloader = mangadex.Mangadex(path='F:\selenium\chromedriver.exe')
downloader.login(username='guest123qwe', password='guest123qwe')
path = downloader.createFolder('F:\manga')

# Download the single chapter
# Use the method numberPage with the link of chapter then download
number = downloader.numberPages(link='https://mangadex.org/chapter/559372/1')
downloader.downloadSelectedChapter(items=number, path=path)
downloader.quit()
