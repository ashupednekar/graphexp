FROM python:3.7
RUN mkdir /learn

COPY . /learn

WORKDIR /learn

RUN python3 -m pip install igraph cairocffi