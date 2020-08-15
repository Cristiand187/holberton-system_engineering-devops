# 0x0F. Load balancer

## :books: Resources
Read or watch:
* [Introduction to load-balancing and HAproxy](https://intranet.hbtn.io/rltoken/ngIXarEyu8jZwOL3Y30PLQ)
* [HTTP header](https://intranet.hbtn.io/rltoken/v32JmcDrSiOnFBfqzXvs_Q)
* [Debian/Ubuntu HAProxy packages](https://intranet.hbtn.io/rltoken/BXGrW_6ocecWaOJb7OK_WA)

---
## :bulb: Learning Objectives
What you should learn from this project:

---
## :computer: Task

### [0. Double the number of webservers](./0-custom_http_response-header)
In this first task you need to configure web-02 to be identical to web-01. Fortunately, you built a Bash script during your web server project, and they’ll now come in handy to easily configure web-02. Remember, always try to automate your work!


### [1. Install your load balancer](./1-install_load_balancer)
Install and configure HAproxy on your lb-01 server.


### [2. Add a custom HTTP header with Puppet](./2-puppet_custom_http_response-header.pp)
Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.
 * The name of the custom HTTP header must be X-Served-By
 * The value of the custom HTTP header must be the hostname of the server Nginx is running on
 * Write 2-puppet_custom_http_response-header.pp so that it configures a brand new Ubuntu machine to the requirements asked in this task

---

## Author
* **Cristian David Pineda Vargas** - [Cristiand187](https://github.com/Cristiand187)