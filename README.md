# json-practice

<a href="https://gitpod.io/#https://github.com/nmagee/json-practice" target="_new"><b>Open with Gitpod</b></a>

Get practice working with JSON:

- [`jq`](jq)
- [Python3](python)
- [data/](data)
- [jsonlint](https://jsonlint.com/)
- [jqplay](https://jqplay.org/#)

An example for fetching JSON from a remote data source:

```
curl https://api.github.com/users/schacon/repos
```

## Compare with XML

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
