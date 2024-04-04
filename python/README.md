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

## Example 2 - TBD Fabricate JSON
