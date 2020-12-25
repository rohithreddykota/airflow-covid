## Steps to run the run the job

- Step 1: Run Docker compose
```
$docker-compose -f docker-compose up
```

- Step 2: Add `Staging postgres` connection
Goto `localhost:8088`: Admin > Connection and add new connection as follows
```
    Conn Id         : postgres_staging
    Connection Type : Postgres
    Host            : staging
    Schema          : staging
    Login           : staging
    Password        : staging
    Port            : 5432
```
![Connection Info](https://github.com/rohithreddykota/airflow-covid/blob/master/.github-meta/Screenshot%202020-12-25%20at%208.35.38%20PM.png)

- Step 3: Turn on the `Covid` DAG

Connect to the postgres database and look for the data in the table `covid_time_series`

```
SELECT * FROM covid_time_series
```

### Dag - Graph View
![Dag Graph View](https://github.com/rohithreddykota/airflow-covid/blob/master/.github-meta/Screenshot%202020-12-25%20at%208.12.56%20PM%20(2).png)
