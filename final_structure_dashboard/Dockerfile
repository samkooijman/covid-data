FROM python:3.7
WORKDIR /src
COPY requirements.txt /
RUN pip install -r /requirements.txt
RUN pip3 install scikit-learn scipy matplotlib
COPY ./ ./
EXPOSE 8080
CMD ["python", "./index1.py"]