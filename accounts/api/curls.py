"""
curl -X POST -d '{"username":"thor", "password":"test"}' http://localhost:8000/account/api/users/login/ -H "Content-Type:application/json"
curl -X GET -H 'Authorization: Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NCwiZXhwIjoxNTIwNTk3OTY0fQ.w5T9dJ9aVUUfRc8jK4Ait7eOPvGKcfTa9Pvn3F2R-zs' http://127.0.0.1:8000/account/api/users/admin/ -H "Content-Type:application/json"
http://127.0.0.1:8000/account/api/users/thor/
"""
