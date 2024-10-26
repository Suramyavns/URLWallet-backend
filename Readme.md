# This is the backend of this small URL shortening project.

## This is how your .env should look like

```
dburl=your-database-url
apiKey=your-api-key #create this yourself
```

## How to run the project

```
pip install -r requirements.txt
python server.py
```

## Run in production

```
gunicorn -w 4 -b 0.0.0.0:<port> app:app
```