### Install:
1. Run `docker-compose up -d --build`. It will build API part and PostgreSQL DB. Settings for DB are in .db_env file
2. Run `docker exec -it nbt_technical_task_web_1 python manage.py migrate` to populate data for checking API
3. Run `docker exec -it nbt_technical_task_web_1 python manage.py fill_fake_data` to populate data for checking API
4. Run `docker exec -it nbt_technical_task_web_1 python manage.py createsuperuser` in case you need to check Django Admin
5. Run `docker exec -it nbt_technical_task_web_1 python manage.py collectstatic` in case you need to check Django Admin


### Notes:
1. Simple API description is available at `http://127.0.0.1:8000/swagger-ui/`
2. In task description second model called Sensor, in model description it's Device :)


### What would I've done next:
1. Move labels[] to other M2M-model in case it could be duplicated
2. Connect git-hook pre-commit to run yapf automatically before commits
3. Close views and docs for logged-in users
4. Fill Swagger with more data and examples of query parameters
5. Add validators for `data` in Measurement