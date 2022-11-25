import urllib.request
contents = urllib.request.urlopen("https://docs.google.com/spreadsheets/d/1Zku_0GSiiBXat7s05JUFeUlP7SeKIEMpBOXYfkfS4BQ/edit?pli=1#gid=0").read()
print(contents)
