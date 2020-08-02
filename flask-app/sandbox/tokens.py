import json
import jwt


pub_key = b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAoDv7GAhqyhSj4q9VnDfCUWTMxOhSHP+AtMaYrO7ByI3dua/DQZapib6qu+CnnR1K1uPHiPeHZ9O1Kkn8RV2m7D72C/tWCm1KDdRX14pbBYR38AR0T5VbYcxblyIPH58okKElWTAWFmGjidY6cXSlO3aEVZMjGB3p2at5o/QfNmCUfxpHivyOnW+b8yLs/h/vXV7EKg4JOLgZ9GV2EiQAZiwJ4pr1a3ttSCjkOVI+F7Gy/yeGeE0VpCDSAcbYuIWSGxB8fFqc58e4xKyLepCdDLFDVHAuIpSXwAwJkqBrwgS4uwNEvQT+INFzZhLEbBsTFKe4wlX3EnyZRMN0D/18rwIDAQAB\n-----END PUBLIC KEY-----'
token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICIzOWd4czh4MmRaYXhPVzdJMFFKRDBENUkzU0kxamw4U0NYcUNHcktXOG80In0.eyJleHAiOjE1OTYzODQyNTcsImlhdCI6MTU5NjM4MDY1NywianRpIjoiMWFlMmI0ZmItOTIyNi00OTc3LWIwYzMtZjRhMzhiMWNiMDNjIiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL2F1dGgvcmVhbG1zL2ZsYXNrLWRlbW8iLCJzdWIiOiJjYWE5NTBiNi0wNjYyLTRhNzUtYmM5ZS02OTE5MzViMjE2YTciLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJmbGFzayIsInNlc3Npb25fc3RhdGUiOiJjYzczZGI4ZS00MDg3LTQ5MmItODJlMS1jOGFhN2E4YWE0ZTciLCJhY3IiOiIxIiwic2NvcGUiOiJlbWFpbCBwcm9maWxlIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJuYW1lIjoiQnJ1Y2UgTGVlIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYnJ1Y2UiLCJnaXZlbl9uYW1lIjoiQnJ1Y2UiLCJmYW1pbHlfbmFtZSI6IkxlZSIsImVtYWlsIjoiYnJ1Y2VAa3VuZy5mdSJ9.N2ujTH1oc1-7xYhLicXEDhB-CguIFIkJhv0PBa_xfKFsFhe68PIlzJNaH0WDE_ddv4nO5aTKcJ083kivDXNx4hCUJKlT7lB3KEwPtQGK3mmde3VYsQjsmxq5JifXIkCmMq1r4iybRRsHWgaay4cOM-vSxtdP46npxLXYsDW1qTFcCw1hybIjgJLJSKR4D_ocnK61oIdNQGovEoFN2_5ph2fnqW3cEP4WaHjQNA5p5DTwMJr5AkSWpl1Bgx5MQgsI1-ItuRg6ld35R2mEB5U7WroguVRqwEDfFncGBkzv1NN-cq4cu48V1COl_XDFy3Y1fRNQIPRwSjF-cVKuaL-hnw'

decoded = jwt.decode(token, pub_key, algorithms=['RS256'])

print(json.dumps(decoded, indent=2))