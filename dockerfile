FROM python:3.12-slim

COPY  frontend.py .

RUN pip install flask requests

EXPOSE 5000
CMD ["python", "frontend.py"]
