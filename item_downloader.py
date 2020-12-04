import csv
import urllib.request


def read():
    """
    Read Csv -> Return List
    """
    line = []
    with open('item_image_urls.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for i in reader:
            line.append(i)
    return line


def download(item_no, url):
    """
    Download item image
    :param item_no: item number
    :param url: item image url
    """
    image_url = 'https://img.29cm.co.kr'+url
    urllib.request.urlretrieve(image_url, f'./static/img/{item_no}.jpg')


if __name__ == '__main__':
    lines = read()
    for idx, line in enumerate(lines):
        try:
            download(line[0], line[1])
            print(idx, line[0])
        except Exception as e:
            print(e)
