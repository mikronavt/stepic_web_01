#!/usr/bin/env bash
#echo "http://localhost/uploads/123"
#curl -I http://localhost/uploads/123
#echo "http://10.42.19.225/js/test.js"
#curl -I http://10.42.19.225/js/test.js
#echo "http://10.42.19.225/uploads/test.js"
#curl -I http://10.42.19.225/uploads/test.js
#echo "http://0.0.0.0/hello/?a=1&a=2&b=3"
#curl "http://0.0.0.0/hello/?a=1&a=2&b=3"
#echo "http://0.0.0.0:8080/?a=1&a=2&b=3"
#curl "http://0.0.0.0:8080/?a=1&a=2&b=3"
curl -vv http://0.0.0.0:8000/login/
curl -vv http://0.0.0.0:8000/question/199/
curl -vv http://10.42.147.197:8000/ask//popular/
curl -vv http://10.42.147.197:8000/blablabla/