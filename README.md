# FastFeria
Proyecto portafolio feria virtual

Para administrar la base de datos en oracle cloud debes ingresar con la cuenta que esta en el Discord.
Y para usar sql debes ingresar con el usuario y la contraseña ubicada en el settings.py



Comando para crear un usuario nuevo de ser necesario ( CREATE USER C##FASTFERIA IDENTIFIED BY 1234;
GRANT CONNECT, RESOURCE TO C##FASTFERIA;
ALTER USER C##FASTFERIA DEFAULT TABLESPACE USERS QUOTA UNLIMITED ON USERS; )
Comando para inspeccionar la base de datos y generar modelos automaticamente: #: py manage.py inspectdb > [app]\models.py



Link drive: https://drive.google.com/file/d/1K-Q1nFzly8YStth-TtT77SpBSGbkHL7f/view?usp=sharing

Para subir los cambios al repositorio, hagan uso de los siguientes comandos en el git bush o cmd:

git add .

git commit -m "text commit"

git remote add origin https://github.com/maruizr/FastFeria.git

git push -u origin master

