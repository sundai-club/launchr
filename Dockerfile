FROM python:3.12-slim
WORKDIR /app

RUN pip install pdm
RUN python -m venv .venv

COPY . .

RUN pdm install --prod

EXPOSE 8501
ENV PYTHONUNBUFFERED=1
CMD ["pdm", "run", "streamlit", "run", "app.py"]
