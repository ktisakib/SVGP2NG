FROM python:3.8-alpine

WORKDIR /var/python

RUN pip3 install \
        ipython \
        cairosvg

CMD ["ipython"]
