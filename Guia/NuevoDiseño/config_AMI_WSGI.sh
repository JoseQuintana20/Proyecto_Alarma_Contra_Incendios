#!/bin/bash

# * ------------------------------------------------------------------------------------
# * "THE BEER-WARE LICENSE" (Revision 42):
# * <diegorestrepoleal@gmail.com> wrote this file. As long as you retain this notice you
# * can do whatever you want with this stuff. If we meet some day, and you think
# * this stuff is worth it, you can buy me a beer in return Diego Andrés Restrepo Leal.
# * ------------------------------------------------------------------------------------


clear

# Color de los mensajes
AZUL=$(tput setaf 6)
VERDE=$(tput setaf 2)
ROJO=$(tput setaf 1)
LILA=$(tput setaf 5)
LIMPIAR=$(tput sgr 0)


instalar_LAMP()
{
    echo
    echo "$VERDE ============= INSTALAR LAMP INICIO ============= $LIMPIAR"
    echo

    echo
    echo "$LILA consultar: https://docs.aws.amazon.com/es_es/AWSEC2/latest/UserGuide/ec2-lamp-amazon-linux-2.html $LIMPIAR"
    echo

    echo
    echo "$AZUL Actualizar $LIMPIAR"
    echo
    sudo yum update -y

    echo
    echo "$AZUL Instalar repositorios de lamp-mariadb10.2-php7.2 y php7.2 $LIMPIAR"
    echo
    sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2

    echo
    echo "$AZUL Instalar PHP, MariaDB y Apache $LIMPIAR"
    echo
    sudo yum install -y httpd mariadb-server

    echo
    echo "$AZUL Iniciar y habilitar servidor web Apache $LIMPIAR"
    echo
    sudo systemctl start httpd
    sudo systemctl enable httpd
    sudo systemctl is-enabled httpd

    echo
    echo "$AZUL Establecer permisos de archivo $LIMPIAR"
    echo
    sudo usermod -a -G apache ec2-user

    echo
    echo "$LILA =============================================== $LIMPIAR"
    echo "$LILA =                Cerrar sesión                = $LIMPIAR"
    echo "$LILA =============================================== $LIMPIAR"
    echo
    touch   ok.txt
    echo
    echo "$VERDE Entre al AMI y ejecute el script nuevamente $LIMPIAR"
    echo

    sleep 10
    exit
}


configurar_MariaDB()
{
    echo
    echo "$VERDE ============= CONTINUACIÓN... ============= $LIMPIAR"
    echo

    echo
    echo "$AZUL Cambiar propiedad de grupo de /var/ww $LIMPIAR"
    echo
    sudo chown -R ec2-user:apache /var/www

    echo
    echo "$AZUL Permisos de escritura de grupo $LIMPIAR"
    echo
    sudo chmod 2775 /var/www && find /var/www -type d -exec sudo chmod 2775 {} \;
    find /var/www -type f -exec sudo chmod 0664 {} \;

    echo
    echo "$AZUL MariaDB $LIMPIAR"
    echo
    sudo systemctl start mariadb
    sudo mysql_secure_installation
    sudo systemctl enable mariadb
}


instalar_WSGI()
{
    echo
    echo "$AZUL Instalar gcc $LIMPIAR"
    echo
    sudo yum install -y gcc

    echo
    echo "$AZUL Instalar httpd-devel $LIMPIAR"
    echo
    sudo yum install -y httpd-devel

    echo
    echo "$AZUL Instalar mod_wsgi $LIMPIAR"
    echo
    sudo yum install -y mod_wsgi

    echo
    echo "$AZUL Instalar tmux $LIMPIAR"
    echo
    sudo yum install -y tmux

    echo
    echo "$AZUL Instalar paquetes de python $LIMPIAR"
    echo
    sudo yum install -y python3-devel
    sudo pip3 install flask
    sudo pip3 install flask-mysql
    sudo pip3 install mysql-connector-python
    sudo pip3 install python-decouple
    sudo pip3 install mod_wsgi
}


configurar_WSGI()
{
    echo
    echo "$AZUL Ingrese IP pública de su AMI $LIMPIAR"
    echo
    read IP

    echo
    echo "$AZUL Ingrese el nombre de su aplicación: sin espacios, sin tildes $LIMPIAR"
    echo
    read NOMBRE
    APLICACION=`echo ${NOMBRE} | tr '[:upper:]' '[:lower:]' | tr ' ' '_'`

    echo "Crear carpeta de la aplicación"
    sudo mkdir -p /var/www/${APLICACION}

    cd /var/www/${APLICACION}

    cat > ${APLICACION}.wsgi <<EOF
#!/bin/python3

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/${APLICACION}")

from ${APLICACION} import app as application
EOF

    cat > ${APLICACION}.py <<EOF
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Este es un mensaje de prueba.'


if __name__ == '__main__':
    app.run()
EOF

    cd /etc/httpd/conf.d

    cat > ${APLICACION}.conf <<EOF
<VirtualHost *:80>
    ServerName ${IP}
    DocumentRoot /var/www/

    WSGIDaemonProcess ${APLICACION} user=apache group=apache threads=5
    WSGIScriptAlias / /var/www/${APLICACION}/${APLICACION}.wsgi

    <Directory /var/www/${APLICACION}/>
        WSGIProcessGroup ${APLICACION}
        WSGIApplicationGroup %{GLOBAL}
        WSGIScriptReloading On
        Options FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>

    ErrorLog /var/log/httpd/error_log
    LogLevel warn
    CustomLog /var/log/httpd/access_log combined

</VirtualHost>
EOF

    sudo updatedb
    MODWSGI=`locate mod_wsgi-py`
    sudo perl -pi -e "s/LoadModule/#LoadModule/" /etc/httpd/conf.modules.d/10-wsgi.conf
    echo "LoadModule wsgi_module \"${MODWSGI}\"" >> /etc/httpd/conf.modules.d/10-wsgi.conf

    sudo systemctl restart httpd

    echo
    echo "$LILA Directorio de la aplicación: $LIMPIAR"
    echo "/var/www/${APLICACION}"
    echo
}


if [ ! -f ok.txt ];
then
    instalar_LAMP
else
    sudo rm -rf ok.txt
    configurar_MariaDB
    instalar_WSGI
    configurar_WSGI
fi


echo
echo "$VERDE FIN $LIMPIAR"
echo


exit 0
