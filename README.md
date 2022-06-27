# simple-https-server
This is a simple HTTPS server to be used in combination with DNS Poisoning and Custom Root CA.
At the moment it only accepts GET and POST requests.

The server logs all it's interactions to the command line, because that is my main use.

## Some explanation
I use this server in my research of Android Apps. Due to the fact that it uses a working and signed certificate it won't raise the self-signed flag.

## Requirements
An active certificate. Letsencrypt is preferred, but any will do.

## Usage
Clone the repository and enter the folder:

    $ git clone https://github.com/NVQXE23I/simple-https-server.git
    $ cd simple-https-server

Create a symbolic link to **fullchain.pem** (*/etc/letsencrypt/live/example.com/fullchain.pem*) with the name **server.pem**.

    $ ln -s /etc/letsencrypt/live/example.com/fullchain.pem server.pem

Create a symbolic link to **privkey.pem** (*/etc/letsencrypt/live/example.com/privkey.pem*) with the name **key.pem**.

    $ ln -s /etc/letsencrypt/live/example.com/privkey.pem key.pem
    
The script can now be run with:

    $ python3 simple_https_server.py
