FROM public.ecr.aws/lambda/python:3.9

WORKDIR /var/task

COPY app.py ./

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["app.lambda_handler"]

