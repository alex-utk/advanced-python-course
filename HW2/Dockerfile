FROM python:3.10.14-slim-bullseye

WORKDIR /usr/src/app

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1

COPY requirements.txt ./
RUN apt-get update \
    && apt-get install  -y \
        texlive-latex-base \
        texlive-latex-extra \
        git nano \
    && python3 -m pip install pipx
RUN pipx install poetry && pipx ensurepath
ENV PATH="${PATH}:/root/.local/bin"
RUN poetry init && poetry add $(cat requirements.txt) 
CMD ["/bin/sh", "-c", "bash"]
