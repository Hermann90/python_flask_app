# pythonflaskapp
flask app to build and test ci/cd pipeline


# flask Application for Student Quiz 

<br>

## Steps to deploy the Application

## STEP 1 : Install python 3
- in our OS (Ubuntu or Windows, --> Install python 3)
- Activate the virtual Env : 
```
mkdir env_project
cd env_project

virtualenv venv 
source venv/bin/activate
```

**1. Clone the project**

```
git clone https://github.com/utrains/pythonflaskapp.git
```

**2. Install Dependencies**

```
pip install -r requirement.txt
```

**3. Run unit test**

```python test_app.py```

**4. Open the port 5000**

```
make sure port 5000 is open.
```

**5. Run the server**

```
python app.py
```

**6. Open following URL in your web browser**

```
127.0.0.1:5000/
```

**7. Run the web based Application test**

```
python test_app_browser.py
```





## Technologies Used

- **Frontend:** python
- **Backend:** flask
