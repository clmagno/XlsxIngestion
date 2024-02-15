# Django Dynamic Model API

This project is a Django REST Framework application that allows users to upload spreadsheet files (.xls or .xlsx) and creates dynamic models based on the contents of the spreadsheets. The application provides an API endpoint for uploading spreadsheets and a browsable API for viewing the data.

## Prerequisites

- Python  3.x
- Django  3.x
- Django REST Framework
- Pandas (for handling spreadsheet files)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/clmagno/XlsxIngestion.git
   ```

2. Navigate to the project directory:

   ```bash
   cd XlsxIngestion
   ```

3. Create a virtual environment and activate it:

   ```bash
   `venv\Scripts\activate`
   ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

### Uploading Spreadsheet Files

To upload a spreadsheet file and create a dynamic model, send a POST request to the `/api/v1/spreadsheet/:tableName/` endpoint with the spreadsheet file and table name.

You can use tools like Postman or curl, or you can create a simple HTML form to upload the file.

### Viewing Data in the Browsable API

Once you have uploaded a spreadsheet and created a dynamic model, you can view the data using the Django REST Framework's browsable API. Navigate to the following URL in your browser:

```
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@path/to/your/spreadsheet.xlsx" -F "table_name=test_table" http://localhost:8000/api/v1/spreadsheet/test_table/
```

Replace `myapp` with the name of your Django app and `test_table` with the name of the dynamic model you created.

### Interacting with the API

The browsable API allows you to interact with your API directly from the browser. You can view, create, update, and delete entries for your dynamic models.

## Development

### Creating Dynamic Models

Dynamic models are created when a user uploads a spreadsheet file. The `create_dynamic_model` function in `myapp/models.py` is responsible for creating the models based on the spreadsheet columns.

### Registering Dynamic Models with the Admin Site

Dynamic models are registered with the Django admin site in `myapp/admin.py`. The `register_models` function ensures that only new models are registered.

### Testing

To test the application, use the Django test framework. Create tests in `myapp/tests.py` and run them with the following command:

```bash
python manage.py test
```

## Deployment

For deployment, follow the standard Django deployment process. This may involve setting up a production-ready web server, configuring a database, and securing your application.

