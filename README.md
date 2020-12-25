## Steps to run the run the job

- Step 1: Run Docker compose
```
$docker-compose -f docker-compose-LocalExecutor up
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

- Step 3: Turn on the `Covid` DAG

Connect to the postgres database and look for the data in the table `covid_time_series`

```
SELECT * FROM covid_time_series
```
