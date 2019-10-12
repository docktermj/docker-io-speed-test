FROM centos:7

# Copy files from repository.

COPY ./artifacts /inside
COPY ./speed-test.py .

# Runtime execution.

CMD ["/speed-test.py"]
