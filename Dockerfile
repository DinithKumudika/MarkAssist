FROM python:3.11.0

#Creates a working directory(app) for the Docker image and container
WORKDIR /usr/src/mark-assist

#Copies the framework and the dependencies for the FastAPI application into the working directory
COPY requirements.txt ./

#Install the framework and the dependencies in the `requirements.txt` file.
RUN pip install --no-cache-dir -r requirements.txt

#Copy the remaining files and the source code from the host `api` folder to the `mark-assist` container working directory
COPY . .

#Expose the FastAPI application on port `8000` inside the container
EXPOSE 5000

ENV PORT 5000

ENV HOST "127.0.0.1"

CMD ["python", "main.py"]