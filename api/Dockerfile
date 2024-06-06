# Basic Python image with FastAPI and Uvicorn
FROM python:3.11

# Set the working directory to /api
ENV WORKDIR=/api
WORKDIR $WORKDIR

# Copy only the requirements file to the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the entire source code to the container
COPY quizzify/ quizzify/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run quizzify.py when the container launches
CMD uvicorn quizzify.main:app --host 0.0.0.0 --port 8000 --log-config quizzify/logging.conf
