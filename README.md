# UK Postcode Validator API

A simple API that validates and formats a UK postcode.

Once you've cloned or downloaded and extracted this repo, you should have a folder structure like this. Please not that that the contents of `uk_postcode_validation_app/` and the inner `uk_postcode_validation_project/` folders were trucated for readability. 

```
uk-postcode-validator-api-main/
├── uk_postcode_validation_project/
│   ├── uk_postcode_validation_app/
│   │   ├── ...
│   ├── uk_postcode_validation_project/
│   │   ├── ...
│   ├── manage.py
├── README.md
├── requirements.txt
```

## Git bash in Windows:
To run locally, setup and activate a virtual environment:

```bash
python -m venv venv
source ./venv/Scripts/activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Change directory to `uk_postcode_validation_project` and run the server:
```bash
cd uk_postcode_validation_project
python manage.py runserver
```

## Bash in Linux:
To run locally, setup and activate a virtual environment:

```bash
python3 -m venv venv
source ./venv/bin/activate
```

Install the requirements:

```bash
pip3 install -r requirements.txt
```

Change directory to `uk_postcode_validation_project` and run the server:
```bash
cd uk_postcode_validation_project
python3 manage.py runserver
```

## Test endpoints

There are two endpoints, one for validating, and another for formatting a postcode. Both enpoints use the GET method and pass the payload `postcode: <string>`

**Validate examples:**

Valid postcode

`http://127.0.0.1:8000/validate_uk_postcode/?postcode=aa9a9aa`

Returns:
```
{
	"postcode": "aa9a 9aa",
	"is_valid": true
}
```

Invalid postcode:

`http://127.0.0.1:8000/validate_uk_postcode/?postcode=foobar`

Returns:
```
{
	"postcode": "foobar",
	"is_valid": false
}
```

**Format example:**

`http://127.0.0.1:8000/format_uk_postcode/?postcode=aa9a9aa`

Returns:
```
{
	"formatted_postcode": "AA9A 9AA"
}
```
