FROM debian:testing
RUN apt-get update && apt-get -y install git
RUN git clone https://github.com/rozie/PlanetJogger.git
