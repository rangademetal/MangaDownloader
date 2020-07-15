# Manga downloader ![version](https://img.shields.io/badge/version-1.1.0-blue.svg)

An python library where you can download the manga from https://mangadex.org with Google Chrome web driver. 
<br/>You can found it here: **https://chromedriver.chromium.org.**


## Mangadex

### Module's Methods

Mangadex(self, path) 

path -> put your path where the Chrome web driver is located
<br/><br/>
**MacOS**
If you got this error "“chromedriver” cannot be opened because the developer cannot be verified". "macOS cannot verify that this app is free from malware."
please follow: https://stackoverflow.com/questions/60362018/macos-catalinav-10-15-3-error-chromedriver-cannot-be-opened-because-the-de
<br/><br/>

## Exemple 1
```diff
# This exemple is used to download the single chapter
- from Downloader import mangadex

- downloader = mangadex.Mangadex(path='F:\selenium\chromedriver.exe')
- downloader.login(username='guest123qwe', password='guest123qwe')
- path = downloader.createFolder('F:\manga')

- number = downloader.numberPages(link='https://mangadex.org/chapter/559372/1')
- downloader.downloadSelectedChapter(items=number, path=path)
- downloader.quit()
```
[See more here](https://github.com/rangademetal/MangaDownloader/blob/master/exemple/exemple1.py)
## Exemple 2
```diff
# This one is used to download all chapters from manga
- from Downloader import mangadex

- downloader = mangadex.Mangadex(path='F:\selenium\chromedriver.exe')
- downloader.login(username='guest123qwe', password='guest123qwe')
- path = downloader.createFolder('F:\manga')

- arr = []
- downloader.getLink('https://mangadex.org/chapter/559372/1')
- n = downloader.numberPagesChapter(items=arr)

- downloader.getLink('https://mangadex.org/chapter/559372/1')
- downloader.downloadAllPages(arr=n, path=path)
```
[See more here](https://github.com/rangademetal/MangaDownloader/blob/master/exemple/exemple2.py)
