import json
import requests




def test_get_requests():
 response = requests.get("http://216.10.245.166/Library/GetBook.php",
                        params={"AuthorName": "Rahul Shetty2"}, )
 response_json = json.loads(response.content)
 print(response_json)

# validation of status code

 print(response.status_code == 200)

# validation of headers
 print(response.headers)
 assert response.headers["Content-Type"] == "application/json;charset=UTF-8"
# validating ISBN no of book -- 23413
 for i in response_json:
    if i['isbn'] == "23413":
        print(i)
        assert i["aisle"] == "75"
        assert i["book_name"]=="Python"




