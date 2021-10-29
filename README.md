# reviewr_api
  After cloning this repo, follow these steps to set up a virtual enviroment:<br/>
  
  1) Install 'virtualenv' on your local system with pip.<br/>
    $ pip install virtualenv<br/>
    
  2) Enter this command in console to create a venv. (Make sure you're inside the same directory where you cloned the repo)<br/>
    $ python -m venv 'venv name'<br/>
    Example: $ python -m venv project-env (Creates a venv named 'project-env'.)<br/>
    
  3) Activate your virtual enviroment<br/>
    $ source 'VENV NAME'/Scripts/activate<br/>
    Example: $ source project-env/Scripts/activate<br/>
    <br/>
    Mac users my need to use this command instead:<br/>
    $ source 'VENV NAME'/bin/activate<br/>
    <br/>
    NOTE: Once your enviroment is activated you should see the name of your VENV in parentheses to the left(or above) the command line in the console. When you want to deactivate your enviroment just enter "deactivate" in the console it's activated in.<br/>
   
   4) Use pip to install the required packages into your venv.(Make sure your VENV is active!)<br/>
    $ pip install -r requirements.txt<br/>
    NOTE: requirements.txt is a configuration file that contains a list of all the packages used in reviewr_api.<br/>

  Running the server:<br/>
  NOTE: During this whole process ensure that your Virutal Enviroment is activated.<br/>
  1) Before you run the Django server for the first time, make sure your database is set up accordingly in settings.py<br/>
  
     NOTE: If using a local database with MySQLWorkbench, make sure the host is localhost(127.0.0.1) and port is 3306. Also the name of the database has to be the exact name of the you one created in MySQLWorkbench. For example, if the database name in setting.py is "reviewr", then create a new database/schema named exactly that in MySQLWorkbench.<br/>
  
  2) Make migrations to add the tables into your database.<br/>
     
     Enter this command first:<br/>
     $ python manage.py makemigrations<br/>
     Then this one:<br/>
     $ python manage.py migrate<br/>
     
     NOTE: If you check the database in MySQLWorkbench, after entering these commands, you will notice the Users and Reviews tables were added, along with other tables that are automatically generated by Django.<br/> 
     
  3) Run the server with this command.<br/>
     $ python manage.py runserver<br/>
     
     The server is reachable from this link: http://127.0.0.1:8000<br/>
     
     NOTE: When navigating the Django server make sure to specify the endpoints you wish to reach in the address bar. Also there is no need to make migrations again, unless you make changes to the models or change to a new/empty database in settings.py<br/>
     For Example: http://127.0.0.1:8000/api/users returns the JSON for all users.
    
    
  
  
  

	
	
  
	
	
	
	
