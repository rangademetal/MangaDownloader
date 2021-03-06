# Manga downloader ![version](https://img.shields.io/badge/version-1.1.0-blue.svg)

An python library where you can download the manga from https://mangadex.org with Google Chrome web driver. This library use **Selenium**.
<br/>You can found it here: **https://chromedriver.chromium.org.**
<br/><br/>
**MacOS Error**<br/>
If you got this error "“chromedriver” cannot be opened because the developer cannot be verified". "macOS cannot verify that this app is free from malware."
please follow: https://stackoverflow.com/questions/60362018/macos-catalinav-10-15-3-error-chromedriver-cannot-be-opened-because-the-de
<br/><br/>


## Mangadex

### Module's Methods

**Constructor**
### Mangadex(self, path) <br/> 
```
path = put your path where the Chrome web driver is located
```
---
### login(self, username, password) <br/>
This method is created because you need to have an account to use the search bar
```
username = Enter your username
password = Enter your password
```
---
### search(self, manga) <br/>
```
manga = Enter your manga's name
```
---
### numberPages(self, link) <br/>
Return the number of pages
```
link = The link where is located your manga chapter 
```
---
### createFolder(self, path)<br/>
Create the new folder with the random numbers name, between 11111111 and 99999999. **Return it as variable**
```
path = Path with location where you want to be your new directory 
```
---
### getLink(self, link)<br/>
Send you to the link address

```
link = Get the link
```
---

### downloadSelectedChapter(self, items, path)<br/>
If you know the number of pages and the path for the directory where was created you can use this method to download only the one chapter 
```
items = The number of pages 
path = The path where is your pages are saved
```
---
### numberPagesChapter(self, items)<br/>
Return the whole numbers of pages from all Chapter as array

```
items = The variable where returned the numbers,mandatory is needed to be array
```
---

### downloadAllPages(self, arr, path)<br/>
Download all the chapters 
```
arr = Give the array when it use from numberPagesChapter(self, items) methods
path = Your directory path
```
---
### quit(self)<br/>
Close the Web driver

---

## Exemple 1
#### This exemple is used to download the single chapter
```
from Downloader import mangadex

downloader = mangadex.Mangadex(path='F:\selenium\chromedriver.exe')
downloader.login(username='guest123qwe', password='guest123qwe')
path = downloader.createFolder('F:\manga')

number = downloader.numberPages(link='https://mangadex.org/chapter/559372/1')
downloader.downloadSelectedChapter(items=number, path=path)
downloader.quit()
```
[See more here](https://github.com/rangademetal/MangaDownloader/blob/master/exemple/exemple1.py)
## Exemple 2
#### This one is used to download all chapters from manga

```
from Downloader import mangadex

downloader = mangadex.Mangadex(path='F:\selenium\chromedriver.exe')
downloader.login(username='guest123qwe', password='guest123qwe')
path = downloader.createFolder('F:\manga')

arr = []
downloader.getLink('https://mangadex.org/chapter/559372/1')
n = downloader.numberPagesChapter(items=arr)

downloader.getLink('https://mangadex.org/chapter/559372/1')
downloader.downloadAllPages(arr=n, path=path)
```
[See more here](https://github.com/rangademetal/MangaDownloader/blob/master/exemple/exemple2.py)
