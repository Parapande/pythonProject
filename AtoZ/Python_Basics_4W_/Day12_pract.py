import json
import requests

from AtoZ.Python_Basics_4W_.Day11_post_data_04 import load_post_data


def test_getx():
    check = requests.get("http://216.10.245.166/Library/GetBook.php",
                         params={"AuthorName": "Parag Pande"})
    print(check.status_code)

    print(check.headers)

    print(check.headers["Server"]=="Apache")

    sdata=json.loads(check.content)
    print(sdata)
    print(type(sdata))

    for i in sdata:
        if i["isbn"]=="bczxdx":
            print(i)
            print(i["book_name"])


def test_postd():

    che=requests.post("http://216.10.245.166/Library/Addbook.php",json=load_post_data())

    fd=json.loads(che.content)

    print(fd)

    for i in fd:
        print(i["Msg"])
