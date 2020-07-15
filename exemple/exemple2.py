from Downloader import mangadex

# Create an object
downloader = mangadex.Mangadex(path='F:\selenium\chromedriver.exe')

# create the dir and save it in path variable
downloader.login(username='guest123qwe', password='guest123qwe')
path = downloader.createFolder('F:\manga')

# Creating the NULL array to save all pages of the manga chapters
# create a new array 
# send the browser on the link
# the method numberPagesChapter return the page number of the chapters
arr = []
downloader.getLink('https://mangadex.org/chapter/559372/1')
n = downloader.numberPagesChapter(items=arr)

# after the pages are knews, the download is started
downloader.getLink('https://mangadex.org/chapter/559372/1')
downloader.downloadAllPages(arr=n, path=path)
