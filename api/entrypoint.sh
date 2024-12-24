#!/bin/bash

# Run the original command and wait for it to finish
uvicorn quizzify.main:app --host 0.0.0.0 --port 8000 --log-config quizzify/logging.conf
