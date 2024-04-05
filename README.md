# json-practice

<a href="https://gitpod.io/#https://github.com/nmagee/json-practice" target="_new"><b>Open with Gitpod</b></a>

Get practice working with JSON:

- [`jq`](jq)
- [Python3](python)
- [data/](data)
- [jsonlint](https://jsonlint.com/)
- [jqplay](https://jqplay.org/#)

Some `curl` examples for fetching JSON from a remote data source:

```
curl https://api.github.com/users/schacon/repos
curl https://api.github.com/repos/nmagee/ds2002-course/branches
```

In Python, either `requests` or `urllib3` can GET remote data.

## 1. Compare with XML

```
{"menu": {
  "id": "file",
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
}}
```

The same text expressed as XML:

```
<menu id="file" value="File">
  <popup>
    <menuitem value="New" onclick="CreateNewDoc()" />
    <menuitem value="Open" onclick="OpenDoc()" />
    <menuitem value="Close" onclick="CloseDoc()" />
  </popup>
</menu>
```

Drawn from https://json.org/example.html

## 2. Work with `jq`

Review the contents of [jq/README.md](jq/README.md) and practice using the CLI to parse JSON.

## 3. Work with Python

Review the contents of [python/README.md](python/README.md) and practice using Python to parse JSON.

