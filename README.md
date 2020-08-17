# Mishipay Back End Developer Programming challenge

Main Task To create a web based server which pulls product information from a Shopify based POS system and updates inventory every time a sale is made.

Must complete
1. Create a Django based web server
2. Integrate with Shopify to retrieve product information from inventory
3. Integrate with Shopify to create an Order with multiple items, on the system such that the inventory gets updated every time and order is created


Login details and auth credentials are shared in the pdf.

Example url:
`https://{api_key}:{password}@mishipaytestdevelopmentemptystore.myshopify.com/admin/api/2020-01/orders.json`


## Installation

```
python3.7 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```


## Development

To run the django server:
```
python manage.py runserver
```

### Docker-compose

To build the docker containers
```
docker-compose build
```

and to run the whole app:
```
docker-compose up
```


## Tests

* For python tests, run 
```
tox testenv
```
from the main directory.


