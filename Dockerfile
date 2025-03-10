FROM python:3.10
WORKDIR /app
COPY . /app/
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install streamlit
COPY . .
EXPOSE 8501
CMD ["python","etl.py"]

