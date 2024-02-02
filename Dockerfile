# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# (You may need to create a requirements.txt file if your script has dependencies)
# RUN pip install --no-cache-dir -r requirements.txt


# Run playlist_sync.py when the container launches
CMD ["python", "playlist_sync.py"]
