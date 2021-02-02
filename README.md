# Covid-19-Monitoring

Monitoring dashboards for covid-19 spanish data  based on Grafana. 

This project is based on containerized services, it will deploy a light orchestration tool `Portainer` in order to make easy the service management but you can go without it. 

## Services

- Portainer: light orchestration tool
- InfluxDB: time series database
- Grafana: dashboard and monitoring solution
- covid-exporter: program coded in Python to get information from the public API built by the [Narrativa team](https://covid19tracking.narrativa.com)

## Deployment with Docker

`docker-compose up -d` (`-d`option is for start the containers in the background)

# Data

In `services/grafana` you will find tow Grafana's dashboard to [import](https://grafana.com/docs/grafana/latest/dashboards/export-import)