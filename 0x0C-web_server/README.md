# 0x0C. Web server

## :books: Resources
Read or watch:
* [How the web works](https://intranet.hbtn.io/rltoken/4tRRzyyETAySzU-bgNGLSw)
* [Nginx](https://intranet.hbtn.io/rltoken/H9OfhUnBDdxV-QQnIucMlA)
* [How to Configure Nginx](https://intranet.hbtn.io/rltoken/wePwmjbJDgJZO7YPvffWxQ)
* [Child process](https://intranet.hbtn.io/rltoken/V8RZRTiBQBweSGFenuQX5w)
* [Root and sub domain](https://intranet.hbtn.io/rltoken/qkpso3mgcpv3tPUhBrZBOA)
* [HTTP requests](https://intranet.hbtn.io/rltoken/C9s3U62JbiOAvn9WCoxKsA)
* [HTTP redirection](https://intranet.hbtn.io/rltoken/kI4vRQ6vc45Wfbdo3UD8Lw)
* [Not found HTTP response code](https://intranet.hbtn.io/rltoken/5UvC588x2hZR7dm6eRFPoQ)
* [Logs files on Linux](https://intranet.hbtn.io/rltoken/bkqQ72HZVAV65G8nB503Pw)

---
## :bulb: Learning Objectives
What you should learn from this project:

* What is the main role of a web server
* What is a child process
* Why web servers usually have a parent process and child processes
* What are the main HTTP requests

---
## :computer: Task

### [0. Transfer a file to your server](./0-transfer_file)
Write a Bash script that transfers a file from our client to a server:
 * Accepts 4 parameters
	 * The path to the file to be transferred
 * The IP of the server we want to transfer the file to
 * The username scp connects with
 * The path to the SSH private key that scp uses
 * Display Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY if less than 3 parameters passed
 * scp must transfer the file to the user home directory ~/
 * Strict host key checking must be disabled when using scp 


### [1. Install nginx web server](./1-install_nginx_web_server)

 * -y on apt-get command


### [2. Setup a domain name](./2-setup_a_domain_name)
.TECH Domains is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. Holberton School partnered with .TECH Domains so that you can learn about DNS.


### [3. Redirection](./3-redirection)
Readme:
 * Replace a line with multiple lines with sed


### [4. Not found page 404](./4-not_found_page_404)
Configure your Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page.


### [5. Design a beautiful 404 page](./5-design_a_beautiful_404_page)
Some of my favorites:
 * Digital Ocean
 * Github
 * Lego
 * Blizzard
 * StickerMule


### [6. Install Nginx web server (w/ Puppet)](./7-puppet_install_nginx_web_server.pp)
Time to practice configuring your server with Puppet! Just as you did before, we’d like you to install and configure an Nginx server using Puppet instead of Bash. To save time and effort, you should also include resources in your manifest to perform a 301 redirect when querying /redirect_me.
 * Nginx should be listening on port 80
 * When querying Nginx at its root / with a GET request (requesting a page)  using curl, it must return a page that contains the string Holberton School
 * The redirection must be a “301 Moved Permanently”
 * Your answer file should be a Puppet manifest containing commands to automatically configure an Ubuntu machine to respect above requirements

---

## Author
* **Cristian David Pineda Vargas** - [Cristiand187](https://github.com/Cristiand187)