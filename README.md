## Start Flask App:

1. Setup DB:
    - In Python interpreter:, 
        - Enter `from app import db`
        - Set up student table: `from app import student`
        - Create DB: `db.create_all()`

2. start the app:
    - `flask run`
    - navigate to http://127.0.0.1:5000/ 

3. Build image:
    - run `docker image build -t docker_flask_app .` from root of project

4. Run docker container:
    - `docker run -p 5000:5000 -d docker_flask_app`


