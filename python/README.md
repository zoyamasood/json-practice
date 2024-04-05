# JSON in Python

As you may already recognize, JSON is quite similar to dictionaries in Python. 
Since JSON is the "language" for machinized exchanges of data, it is important
to be able to retrieve, parse, and generate JSON using Python.

## Example 1 - Pull and Read JSON

```
import requests

url = "https://api.github.com/repos/nmagee/ds2002-course/branches"

response = requests.get(url)

# get out the name objects
for r in response.json():
  print(r['name'])
```

If you run the first three commands of this Python interactively you now have an object populated with all artifacts of the request and other methods.

```
>>> import requests
>>> url = "https://api.github.com/repos/nmagee/ds2002-course/branches"
>>> response = requests.get(url)

>>> response.
response.apparent_encoding     response.history               response.ok                   
response.close(                response.is_permanent_redirect response.raise_for_status(    
response.connection            response.is_redirect           response.raw                  
response.content               response.iter_content(         response.reason               
response.cookies               response.iter_lines(           response.request              
response.elapsed               response.json(                 response.status_code          
response.encoding              response.links                 response.text                 
response.headers               response.next                  response.url
``` 

Some important elements about the request:

- `response.encoding` - `'utf-8'`
- `response.headers` - HTTP response headers about the request/reply.
- `response.status_code` - `200` is OK; other status codes indicate errors.
- `response.request.*` - Request method, URL, headers, body, etc. about the original request.
- `response.text` - Text version of the actual data response. Quote-wrapped.
- `response.json()` - Native JSON of the data response. This is often `[ ]` wrapped indicating an array within the response that should be iterated apart.

```
>>> response.json()
[{'name': 'container', 'commit': {'sha': '0caa8d395b834613ef35571ceec8ef01fdbc2518', 'url': 'https://api.github.com/repos/nmagee/ds2002-course/commits/0caa8d395b834613ef35571ceec8ef01fdbc2518'}, 'protected': False}, {'name': 'main', 'commit': {'sha': '4719cdbb60d1a180d2afde1947c097e80c7c13d1', 'url': 'https://api.github.com/repos/nmagee/ds2002-course/commits/4719cdbb60d1a180d2afde1947c097e80c7c13d1'}, 'protected': False}]

>>> payload = response.json()
>>> for p in payload:
>>>   print(p['name'])
container
main
```

## Example 2 - TBD Fabricate JSON
