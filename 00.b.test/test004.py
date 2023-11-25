import requests
import json

url = "http://10.41.116.3:8889/v1/oauth/token"

payload = json.dumps({
   "client_id": "50085276810219520",
   "client_secret": "7375055ea3d7190aa6910ea5ceec7a15",
   "grant_type": "password",
   "username": "admin",
   "password": "SjOxRB++EG69ovnQt/4zJJt2NjtTrveTjN6HRtr4/6n+biK7AaP9Lae8rKj5DOmZUIj0TRFmN5Z1oEexaDy0CWPtO4NBlV9753Mu7MtBJ7pRJtd/zHUZ8W/C9OtGa7xwVFXjZkb+miY6tzUxheFPFrUBc3FPTcYA/2u//JzfYVw="
})
headers = {
   'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
