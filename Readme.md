# OctoBI Assignment

```
DataFormatting.py (DataFormatting.ipynb): Notebook used to format data
```

## Completed Parts

- [x] Seperate Data in to Different models
- [x] Implement models in the Django application
- [x] Format data and clean data
- [x] Import data using django Fixtures (except for summary)
- [x] Implement basic views
- [ ] Display Table Structure and data points
- [x] Dockerize the solution
- [ ] Test the solution (TDD)

## How to setup

1. Copy dataset in the CSV file to the root folder
2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Migrate the application

```
python manage.py migrate
```

5. Format and load data by running `format.sh` file
6. Run the server

```bash
python manage.py runserver
```
