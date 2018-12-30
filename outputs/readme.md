# Outputs
The files in output are in a bulk format. 
You can use those file directly in a bulk request.

# Indexations

Make sure that Elasticsearch is running on the port 9200 on localhost
Then type the following to index the messages:

```
curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/_bulk --data-binary "@messages.json"
```