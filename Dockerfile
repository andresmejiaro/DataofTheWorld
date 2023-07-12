FROM debian:bookworm 

RUN apt update && apt install -y \
	curl \
	python3 \
	python3-pip \
	python3-venv && rm -rf /var/lib/apt/lists/*
RUN python3 -m venv venv
RUN /venv/bin/python -m pip install dash plotly pandas dash-core-components

COPY UN_WPP2022_GEN_F01_DEMOGRAPHIC_INDICATORS_COMPACT_REV1.csv /csv/

EXPOSE 8050

#docker run -it debian:bookworm /bin/bash