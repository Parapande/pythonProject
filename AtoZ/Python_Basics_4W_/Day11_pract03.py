import json
import requests

# run in pytest for get request
from AtoZ.Python_Basics_4W_.Day11_post_data_04 import load_post_data


def test_get():
    res = requests.get("http://216.10.245.166/Library/GetBook.php",
                       params={"AuthorName": "Parag Pande"})
    print(res.status_code)

    # assertions used for valid status code
    assert res.status_code == 200

    print(res.headers)

    print(res.headers["Server"])

    assert res.headers["Server"] == "Apache"

    # validation of body pass the json to str or dict format

    pydata = json.loads(res.content)
    # to check data type and data is convert or not

    print(type(pydata))

    print(pydata)

    # valdation of isbn=bczxdx also check book_name
    # use loop for list to dict itration

    for i in pydata:
        if i["isbn"] == "bczxdx":
            print(i)
            # vai assertion
            assert i["book_name"] == "Learn with Parag"
            break


def test_datap():
    # post the data json patload

    response = requests.post("http://216.10.245.166/Library/Addbook.php",
                             json=load_post_data())
    print(response.status_code)
    # via assertions
    assert response.status_code == 200

    # validating headers

    print(response.headers)
    assert response.headers["Content-Type"] == "application/json;charset=UTF-8"

    # covert json data or parse data

    pdata = json.loads(response.content)

    print(type(pdata))
    print(pdata)

    # to check new data is added or not
    assert pdata["Msg"]=="successfully added"
