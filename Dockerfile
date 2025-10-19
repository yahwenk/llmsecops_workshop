FROM python:3.10-slim
# Set the working directory in the container
WORKDIR /app
# Copy only the requirements file to leverage Docker cache
COPY requirements.txt .
# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the application code to the working directory
COPY . .
# Expose port 8000
EXPOSE 8000
# Use a minimal entrypoint and CMD
ENTRYPOINT ["python"]
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]