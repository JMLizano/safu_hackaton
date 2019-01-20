# Safu hackaton

Web interface to quickly check via API whether a public address is safe, i.e. not associated with any scam or fraud and incentivize contributors to share bad (hacked or malicious) addresses, together with proof, to help the SAFU Address Platform increase its address database

## Endpoints

**GET /api/address/{ids}**
---
Return a list of address

{ids}: Comma separated list of address ids.

**GET /api/transaction/<id>**
---
Return a list of transactions

<id>: Id of the transaction


**POST /api/submit/**
---
Submit a suspicious address for further investigation



## Development

The project is developed in Python 3.4, using the Flask web microframework. A makefile is provided to ease the use.


* **Running the project locally:**

``` bash
$ make install
$ make run
```

Note that you will have to set the appropiate environment variables in a .env file, before be able to run the project. A '.env.example' is provided as template.