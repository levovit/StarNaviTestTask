FROM python:3.11-alpine AS base

WORKDIR .

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM base AS development

EXPOSE 8000

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["/bin/sh", "-c", "./entrypoint.sh"]

FROM base AS test

ENTRYPOINT ["pytest", "tests"]

