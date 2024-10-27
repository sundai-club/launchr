FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml pdm.lock .
RUN pip install pdm && pdm install --prod
COPY . .
EXPOSE 8501
ENV PYTHONUNBUFFERED=1
CMD ["streamlit", "run", "app.py"]
