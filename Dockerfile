From frolvlad/alpine-python2
RUN apk --update add gcc python-dev musl-dev
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ADD run.py /app/run.py
ADD layer.py /app/layer.py
#ENTRYPOINT ["yowsup-cli"]

