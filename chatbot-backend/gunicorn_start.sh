#!/bin/bash
# Start Gunicorn processes
echo "Starting Gunicorn."
exec gunicorn --bind=0.0.0.0:8000 app:app
