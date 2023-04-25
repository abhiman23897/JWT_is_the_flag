#Setting up frontend
FROM node:18-alpine AS frontend

WORKDIR /ctf-app
COPY ctf-app/public/ /ctf-app/public
COPY ctf-app/src/ /ctf-app/src
COPY ctf-app/package.json /ctf-app
RUN npm install
RUN npm install -g serve
RUN npm run build

#Setting up backend
FROM python:3.9-alpine AS backend

COPY --from=frontend /ctf-app/build /app/static

WORKDIR /app
COPY requirements.txt app.py /app
COPY images/ /app/images
COPY --from=frontend /ctf-app/build/static /app/static

RUN rm -rf /app/static/static
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

#Run the backend
CMD ["python", "app.py"]