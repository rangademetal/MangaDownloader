# Manga downloader ![version](https://img.shields.io/badge/version-1.1.0-blue.svg)

An python library where you can download the manga from https://mangadex.org with Google Chrome web driver. 
<br/>You can found it here: **https://chromedriver.chromium.org.**


## Mangadex

### Constructor

<font size=14>Mangadex(self, path) </font><br/>
path -> put your path where the Chrome web driver is located
<br/><br/>
**MacOS**
If you got this error "“chromedriver” cannot be opened because the developer cannot be verified". "macOS cannot verify that this app is free from malware."
please follow: https://stackoverflow.com/questions/60362018/macos-catalinav-10-15-3-error-chromedriver-cannot-be-opened-because-the-de
<br/><br/>

### Methods

|        Name methods     |      Parameter     | Description |
|-------------------------|--------------------|-------------|
| login(username, password)| username           | Your username account |
|                           | password           | Your password account |
| search(manga)      | manga | Input the name's manga you wish to read |
| DownloadSelectedChapter(link, path) | link | Initialization with link the chapter |
|                                     | path | Location where is saved |


## Exemple 1
from Downloader import mangadex

downloader = mangadex.Mangadex(path='F:\selenium\chromedriver.exe')
downloader.login(username='guest123qwe', password='guest123qwe')
path = downloader.createFolder('F:\manga')

number = downloader.numberPages(link='https://mangadex.org/chapter/559372/1')
downloader.downloadSelectedChapter(items=number, path=path)
downloader.quit()
