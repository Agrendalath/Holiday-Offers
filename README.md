# Holiday Offers
[![CircleCI](https://circleci.com/gh/Agrendalath/Holiday-Offers.svg?style=svg)](https://circleci.com/gh/Agrendalath/Holiday-Offers)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

A simple Flask API for filtering holiday offers retrieved from external API.

## Manual usage
### Installing
This project uses [Pipenv](https://github.com/pypa/pipenv) for dependency management. To install it, please follow [Pipenv installation guide](https://docs.pipenv.org/install/).
To install dependencies, run:

    pipenv sync

### Testing
To install dependencies for testing, run:
    
    pipenv sync --dev

To run tests, run:

    pipenv run coverage run -m pytest
    
To see coverage, run:
    
    pipenv run coverage report

    
#### Linters
To run formatting checks (pylint and black), run:

    pipenv run pylint holiday_offers
    pipenv run black --check holiday_offers


### Running
You can run the API manually with:

    FLASK_APP=holiday_offers/app.py \
    FLASK_ENV=development \
    FLASK_DEBUG=1 \
    pipenv run flask run --host=0.0.0.0

## Docker
### Tests
To run tests in Docker container, issue:

     docker-compose up docker-compose -f local-test.yml up

### Local
To run API locally, you can use:

    docker-compose up docker-compose -f local.yml up

### Production
The production config is in `production.yml` file. If you want to run it locally, create `.env` file with `URL=0.0.0.0:443` and start server by issuing:

    docker-compose up docker-compose -f production.yml up
    
For convenience, there is a ready server setup in `production_setup` directory. You can simply copy it to your server, create `.env` file with your own domain, and run

    docker-compose up -d
    
in a directory with the config. The server will also be automatically started with Docker system service.

#### Updating
To update your instance manually, you can use `update.sh` script.


## Endpoints
The only endpoint retrieves data from external API. You can use query params for filtering results.
* **URL**
    
    `/`
    
* **Method:**
    
    `GET`
    
* **URL Params**

    * `earliest_departure_time = [%H:%M]`
    * `earliest_return_time = [%H:%M]`
    * `max_price = [numeric]`
    * `min_price = [numeric]`
    * `star_rating = [numeric]`

* **Success Response:**
    * **Code:** 200 OK<br/>
    **Content:**
    
    ```json
    {
      "offers": [
        {
          "Hotelname": "Catalonia+Punta+Del+Rey", 
          "Inboundarr": "23/08/2018 00:20", 
          "Inbounddep": "22/08/2018 20:05", 
          "Inboundfltnum": "LS1664", 
          "Outboundfltnum": "LS1663", 
          "Sellprice": "510.62", 
          "Starrating": "4"
        }, 
        {
          "Hotelname": "Catalonia+Las+Vegas", 
          "Inboundarr": "23/08/2018 00:20", 
          "Inbounddep": "22/08/2018 20:05", 
          "Inboundfltnum": "LS1664", 
          "Outboundfltnum": "LS1663", 
          "Sellprice": "518.81", 
          "Starrating": "4"
        }
      ], 
      "summary": {
        "average_price": "514.71", 
        "cheapest_price": "510.62", 
        "most_expensive_price": "518.81"
      }
    }
    ```
    
* **Error Response:**
    * **Code:** 400 Bad Request<br/>
    **Content**: "Unknown parameter: {key}"
    
        *OR*
        
    * **Code:** 400 Bad Request<br/>
    **Content**: "{value} is not valid value for {key}"

        *OR*
        
    * **Code:** 400 Bad Request<br/>
    **Content**: "Invalid time format for {key}"
