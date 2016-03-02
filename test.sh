#!/usr/bin/env bash
echo "http://localhost/uploads/123"
curl -I http://localhost/uploads/123
echo "http://10.42.19.225/js/test.js"
curl -I http://10.42.19.225/js/test.js
echo "http://10.42.19.225/uploads/test.js"
curl -I http://10.42.19.225/uploads/test.js