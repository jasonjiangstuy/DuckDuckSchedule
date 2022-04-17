import requests

def viewDB():
    url = "https://alchera-face-authentication.p.rapidapi.com/v1/face"

    headers = {
        "X-RapidAPI-Host": "alchera-face-authentication.p.rapidapi.com",
        "X-RapidAPI-Key": "bb36e4099cmsh366bb70ec0baea4p1ac84ejsna1bd5115daad"
    }

    response = requests.request("GET", url, headers=headers)

    return (response.text)

def RegisterFace(name, imageURL):
    import requests

    url = "https://alchera-face-authentication.p.rapidapi.com/v1/face"

    payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\""+ imageURL+"\"\r\n\r\n\r\n-----011000010111000001101001--\r\n\r\n"
    headers = {
        "content-type": "multipart/form-data; boundary=---011000010111000001101001",
        "uid": name,
        "X-RapidAPI-Host": "alchera-face-authentication.p.rapidapi.com",
        "X-RapidAPI-Key": "bb36e4099cmsh366bb70ec0baea4p1ac84ejsna1bd5115daad"
    }
    print("SENDING")
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)