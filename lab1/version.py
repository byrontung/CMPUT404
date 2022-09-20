import requests

def main():
    # print(requests.__version__)
    # homepage = requests.get("http://www.google.com/")
    # https://github.com/byrontung/CMPUT404/blob/main/lab1/version.py
    content = requests.get("https://github.com/byrontung/CMPUT404/blob/main/lab1/version.py")
    print(content)

if __name__ == "__main__":
    main()