from urllib.robotparser import RequestRate
import requests

def main():
    # print(requests.__version__)
    homepage = requests.get("http://www.google.com/")
    print(homepage)

if __name__ == "__main__":
    main()