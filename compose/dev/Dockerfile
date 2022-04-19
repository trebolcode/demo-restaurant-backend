FROM python:3.9
ENV PYTHONUNBUFFERED 1

#Directory work
WORKDIR /usr/src/app

#Copy requirements files
COPY requirements.txt ./

# Install 
RUN python3.9 -m pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# Excecute program
CMD python3.9 main.py