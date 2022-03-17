FROM python:3.8-buster

COPY ./ /maris_cdi
WORKDIR /maris_cdi

RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    python setup.py install

ENTRYPOINT ["maris_cdi"]
