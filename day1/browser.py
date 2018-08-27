import webbrowser

keywords = ["아이유", "설현", "수지"]
url = "https://search.naver.com/search.naver?query="

for name in keywords:
    webbrowser.open(url+ name)
