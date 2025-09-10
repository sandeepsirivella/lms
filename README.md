//deploying a simple frontend application using flask and html//

```#git clone https://github.com/sandeepsirivella/lms.git
#ls
#cd lms
#apt update
#apt install -y python3 python3-pip python3-venv
#apt install -y nginx
#cd lms
#python3 -m venv myvenv
#ls
#source myvenv/bin/activate
#ls
#pip install flask
#pip install gunicorn
#gunicorn --bind 0.0.0.0:8000 app:app
#sudo vi /etc/nginx/sites-available/lms
//configuration file//
server {
    listen 80;
    server_name 16.170.246.164 (server_public_ip) ;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

#sudo ln -s /etc/nginx/sites-available/lms /etc/nginx/sites-enabled/
#sudo nginx -t
#sudo systemctl reload nginx
#sudo vi /etc/systemd/system/lms.service
//lms.service file //
[Unit]
Description=Gunicorn instance to serve  LMS
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/lms
Environment="PATH=/lms/myvenv/bin"
ExecStart=/lms/myvenv/bin/gunicorn --workers 3 --bind 127.0.0.1:8000 app:app

[Install]
WantedBy=multi-user.target

#sudo systemctl daemon-reexec
#sudo systemctl enable lms
#sudo systemctl start lms
#systemctl status lms

//if you get templates not found error// //we have to keep index.html inside templates folder Flask  by default searches templates in the  default templates folder//  
#mkdir -p /lms/templates
#mv /lms/index.html /lms/templates/index.html
#sudo systemctl restart lms'''


<img width="1920" height="1080" alt="Screenshot (178)" src="https://raw.githubusercontent.com/user-attachments/assets/c7d392a4-eff0-435e-b8a9-634cef85ed9b" />
