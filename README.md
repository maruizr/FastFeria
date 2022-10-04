# FastFeria
Proyecto portafolio feria virtual

Primero descargar la base de datos Oracle 21C XE en el siguiente link (El primer link de descarga):

https://www.oracle.com/cl/database/technologies/xe-downloads.html

Segundo se debe crear el usuario con los siguientes comandos en el programa de SQL developer:

CREATE USER C##FASTFERIA IDENTIFIED BY 1234;
GRANT CONNECT, RESOURCE TO C##FASTFERIA;
ALTER USER C##FASTFERIA DEFAULT TABLESPACE USERS QUOTA UNLIMITED ON USERS;

Luego ejecutar el scripts de las tablas adjuntado en el archivo de texto: "Script_Crea_Tablas"

Link drive: https://drive.google.com/file/d/1K-Q1nFzly8YStth-TtT77SpBSGbkHL7f/view?usp=sharing

Para subir los cambios al repositorio, hagan uso de los siguientes comandos en el git bush o cmd:

git add .

git commit -m "text commit"

git remote add origin https://github.com/maruizr/FastFeria.git

git push -u origin master

