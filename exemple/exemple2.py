from Downloader import mangadex

# Create an object
downloader = mangadex.Mangadex(path='F:\selenium\chromedriver.exe')
#
downloader.login(username='guest123qwe', password='guest123qwe')
# create the dir and save it in path variable
path = downloader.createFolder('F:\manga')

# Creating the NULL array to save all pages of manga chapters
# create a new array 
arr = []
# send the browser on the link
downloader.getLink('https://mangadex.org/chapter/559372/1')
# this method return the page of chapters
n = downloader.numberPagesChapter(items=arr)

# after the pages are knews, the download is started
downloader.getLink('https://mangadex.org/chapter/559372/1')
# After knows the all pages, the download has begin
downloader.downloadAllPages(arr=n, path=path)
