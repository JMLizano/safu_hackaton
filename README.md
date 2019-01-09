# Safu hackaton

Web interface to quickly check (via API or website) whether a public address is safe, i.e. not associated with any scam or fraud and incentivize contributors to share bad (hacked or malicious) addresses, together with proof, to help the SAFU Address Platform increase its address database

## Endpoints

**Home**
---
Exposes a web page to check for the score of an address.

* **Url:**

  `GET | POST` `/`

* **Body:**

``` js
Content-Disposition: form-data; name="address"

address1
```


**Submit**
---
To inform of a malicius address


* **Url:**

  `GET | POST` `/submit`

* **Body:**

``` js
Content-Disposition: form-data; name="address"

address1
```
## Development

The project is developed in Python 3.6, using the Flask web microframework. A makefile is provided to ease the use.

* **Running the project locally:**

``` bash
$ make install
$ make run
```

Note that you will have to set the appropiate environment variables in a .env file, before be able to run the project. A '.env.example' is provided as template.

### Deployment 

The project is deployed in a serverless fashion, using AWS Lambda + AWS API Gateway services and the [zappa framework](https://github.com/Miserlou/Zappa)