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
pip install -r requirments.txt
```

Run the server:
```bash
python manage.py runserver
```

## Git bash in Windows:
To run locally, setup and activate a virtual environment:

```bash
python -m venv venv
source ./venv/Scripts/activate
```

Install the requirements:

```bash
pip install -r requirments.txt
```

Run the server:
```bash
python manage.py runserver
```



## test endpoints

http://127.0.0.1:8000/validate_uk_postcode/?postcode=aa9a9aa

{
	"postcode": "aa9a 9aa",
	"is_valid": true
}

{
	"postcode": "foobar",
	"is_valid": false
}


http://127.0.0.1:8000/format_uk_postcode/?postcode=aa9a9aa

{
	"formatted_postcode": "AA9A 9AA"
}

