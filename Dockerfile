FROM python:3.14-slim

WORKDIR /app

COPY dist/*.whl /wheels/

RUN python -m pip install --no-cache-dir /wheels/*.whl gunicorn

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "restaurant.app:app"]