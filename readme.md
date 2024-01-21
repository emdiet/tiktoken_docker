# tiktoken docker image: cl100k_base

cl100k_base tokenizer with an http endpoint wrapped into a docker container.

convenient for OpenAI based node.js projects that need to tokenize text - just add it to your docker-compose network.

docker image: https://hub.docker.com/r/emdiet/tiktoken/tags

fastapi documentation: http://localhost:7170/docs

# /encode API Endpoint

## POST `/encode`

Encode a string.

### Request

#### Request Body

- Content type: `application/json`

##### Example Value

```json
{
  "text": "string"
}
```

##### Curl
```bash
curl -X 'POST' \
  'http://localhost:7170/encode' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "hello world!"
}'
```
##### Request URL
```
http://localhost:7170/encode
```
##### Response

```json
[
  15339,
  1917,
  0
]
```
###### Response Headers

```text
 content-length: 14 
 content-type: application/json 
 date: Sun,21 Jan 2024 01:51:17 GMT 
 server: uvicorn 
```

# /decode API Endpoint

## POST `/decode`

decode an embedding.

### Request

#### Request Body

- Content type: `application/json`

##### Example Value

```json
{
  "encoded": [
    15339,
    1917,
    0
  ]
}
```

##### Curl
```bash
curl -X 'POST' \
  'http://localhost:7170/decode' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "encoded": [
    15339,
    1917,
    0
  ]
}'
```
##### Request URL
```
http://localhost:7170/decode
```

##### Response

```json
"hello world!"
```
###### Response Headers

```text
 content-length: 14 
 content-type: application/json 
 date: Sun,21 Jan 2024 01:54:59 GMT 
 server: uvicorn 
```
