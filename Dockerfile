# first stage
FROM python:3.9 AS builder
COPY requirements.txt .

# install dependencies to the local user directory (eg. /root/.local)
RUN pip3 install --user -r requirements.txt

# second unnamed stage
FROM python:3.9-slim
WORKDIR /src

# copy only the dependencies installation from the 1st stage image
COPY --from=builder /root/.local /root/.local
RUN apt-get update && apt-get install libpq5 -y
COPY ./src .