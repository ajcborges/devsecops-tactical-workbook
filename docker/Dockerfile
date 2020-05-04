FROM python:3.8.2-buster

ADD . /book
WORKDIR /book
RUN make python
RUN if [ ! -d "pygments-css" ]; then git clone https://github.com/richleland/pygments-css.git; fi; \
cp /book/pygments-css/vim.css /book/docs/theme/static/
RUN make docs
