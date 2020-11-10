import os
import requests
import sys
from bs4 import BeautifulSoup
# Please note that requests and bs4 libraries are not available in the standard library.
# You will have to install bs4 and requests using command prompt(pip).

# write your code here
args = sys.argv
directory = args[1]
if not os.path.exists(directory):
    os.mkdir(directory)
# The above code is for specifying the directory in which the web pages will be stored.
# You should comment the above lines if you're trying to run the code in the Python terminal.

stack = []
file_stack = dict()
while True:
    url = input()
    if ".com" in url:
        url_copy = url.rstrip(".com")
    else:
        url_copy = url.rstrip(".org")
    if url == "exit":
        break

    elif url == "back":
        print(stack[-2].get_text())

    elif url == url_copy:
        for i in file_stack:
            if i == url:
                with open(file_stack[url], "r") as file1:
                    for line in file1:
                        print(line)

    elif (".com" in url) or (".org" in url):
        r = requests.get("https://" + url)
        if r:
            soup = BeautifulSoup(r.content, "html.parser")
            new_soup = soup.find_all("html")
            for water in new_soup:
                print(water.get_text())
            url = os.path.join(directory, url_copy + ".txt")
            with open(url, "w") as file1:
                for water in new_soup:
                    file1.write(water.get_text())
            stack.append(new_soup)
            file_stack[url_copy] = url

        else:
            print("Error: Incorrect URL")
