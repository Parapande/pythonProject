import json
import requests




def test_get_requests():
    response = requests.get("http://216.10.245.166//Library/GetBook.php",
                            params={"AuthorName": "Ashish Sonone"}, )

    response_json = json.loads(response.content)

    # validating status code
    assert response.status_code == 200

    # validating headers
    print(response.headers)
    assert response.headers["Content-Type"] == "application/json;charset=UTF-8"

    # validating ISBN no of book -- 23413
    print(response_json)
    for i in response_json:
        if i["isbn"] == "23413":
            # print(i)
            # validating book name , aisle
            assert i["book_name"] == "Python"
            assert i["aisle"] == "75"
            break


def test_post_request():
    response = requests.post("http://216.10.245.166/Library/Addbook.php",
                             json=patload_post_data())

    # validating response code
    assert response.status_code == 200
    print(response.status_code)

    # parse response into json format
    response_json = json.loads(response.content)
    print(type(response_json))
    print(response_json)

    # validating response msg
    assert response_json["Msg"] == "successfully added"

    # grab ID generated for new book
    new_book_id = (response_json["ID"])
    print(new_book_id)


def test_retriving_books():
    response = requests.get("http://216.10.245.166/Library/GetBook.php",
                            params={"AuthorName": "Ashish Sonone"}, )
    # validating response code
    assert response.status_code == 200

    # converting data in to jason format

    response_json = json.loads(response.text)
    print(response_json)

    # validating book ISBN
    for i in response_json:
        if i["isbn"] == "bcdasss":
            print(i["book_name"])
            assert i["book_name"] == "Learn api with python"
            break


def test_updating_data():
    response = requests.put("https://fakestoreapi.com/products/1",
                            json=updating_payload(), )

    print(response.status_code)

    # converting response to json_response
    response_json = json.loads(response.text)

    print(response_json)
    assert response_json["id"] == 1


def test_deleting_data():
    response = requests.delete("https://fakestoreapi.com/products/1")

    # validating response code
    print(response.status_code)
    assert response.status_code == 200

    # converting to json format

    response_json = json.loads(response.text)
    print(response_json)

    # title validationemaile
    assert response_json["title"] == "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops"


# request body /request payload
def patload_post_data():
    body = {
        "name": "Learn api - with - Python",
        "isbn": "1lh",
        "aisle": "asd",
        "author": "Ashish Sonone"

    }
    return body


def updating_payload():
    body = {

        "id": 4,
        "title": "the_crafty-angels",
        "price": 15.99,
        "description": "3 layer explosion box",
        "image": "https://fakestoreapi.com/img/71YXzeOuslL._AC_UY879_.jpg",
        "rating": {
            "rate": 2.1,
            "count": 430
        }
    }


