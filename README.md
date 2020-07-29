# Keycloak

Get a token:
```
$ curl -s -d 'client_id=flask' -d 'username=bruce' -d 'password=bruce' -d 'grant_type=password' -d 'client_secret=a12ecbf6-b954-4059-95d3-24a8a4909995' keycloak:8080/auth/realms/flask-demo/protocol/openid-connect/token | jq
```

Fire up Busybox (including `curl`):
```
$ kubectl run curl --image=radial/busyboxplus:curl -i --tty --rm
```

# Flask

Use the token to access a restricted endpoint:
```
$ curl -i -H "Authorization: Bearer <token>" "http://flask-app:5000/api/user/info"
```
