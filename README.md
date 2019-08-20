# test_celery
Celery rabbitmq testing

#### First clone the repo 
git clone https://github.com/daedalus/test_celery

#### In a separate terminal
python3 /usr/local/bin/celery -A test_celery worker --loglevel=info

#### In another terminal

python3 -m test_celery.run_tasks
