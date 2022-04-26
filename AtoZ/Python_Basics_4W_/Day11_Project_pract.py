import json
import requests


# for get requests we have add the base url with parameters

def get_requests():
    response = requests.get("http://216.10.245.166//Library/GetBook.php",
                            params={"AuthorName": "Ashish Sonone"}, )

    response_json = json.loads(response.content)

    # validating status code
    assert response.status_code == 200

    # validating headers
    print(response.headers)
    assert response.headers["Content-Type"] == "application/json;charset=UTF-8"
