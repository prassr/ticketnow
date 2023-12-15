# Ticket Now

A Ticket Show App

* Root folder 
  - ` ~/ticketnow `

* Running Flask Server

  - ` ~/ticketnow/src ` contains flask application specific files and folder.

```bash
~/ticketnow/src/ $ ./run
```

* Running Redis Server

```bash
~$ redis-server
```

* Running Celery worker

```bash
~/ticketnow/src/ $ celery -A app:capp worker -l INFO # logleve info
```

* Running Celery beat


```bash
~/ticketnow/src/ $ celery -A app:capp beat -l INFO # logleve info
```

* Running Vue Application Server


    - ` ~/tickenow/ticketnow ` contains files for vue frontend.

```bash
~/ticketnow/ticketnow $ sudo vue serve
```
