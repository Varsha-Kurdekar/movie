# Use official Python image 
FROM python:3.12-slim

# Set working directory
WORKDIR /movie_theatre

# Copy all files to container
COPY . .

# Command to run python file
CMD ["python", "movie_theatre.py"] 