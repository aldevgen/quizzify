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

# Copy the entrypoint script to the container
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run entrypoint.sh when the container launches
CMD ["./entrypoint.sh"]
