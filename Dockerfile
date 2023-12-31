FROM python:3.10

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN python -m pip install --no-cache-dir poetry==1.7.1 \
    && poetry config virtualenvs.create false \
    && poetry install --without dev,test --no-interaction --no-ansi \
    && rm -rf $(poetry config cache-dir)/{cache,artifacts}

COPY . /app

EXPOSE 8000

# CMD or ENTRYPOINT
# Comment entrypoint, if you don't have migrations 

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# ENTRYPOINT [ "/app/entrypoint.sh" ]