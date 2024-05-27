﻿
Name: 		zzClusterEm
Version:	1.0
License:	MIT
Author:		Carlo Bisda

zzClusterEm is a simple CLI email marketing tool that will send your email to your email list one by one
with a file attachment.

CONFIG:
Make sure to edit the config files for your customized email addresses and messages.

config.ini
    sender_email=youremailaddress@whatever.com
    sender_password=Password
    smtp_server=smtp-mail.outlook.com
    smtp_port=587
    subject=Your Email Subject

filename.ini
    xxxx.pdf (can be whatever file that can be sent over via email)

list.ini
    whateveremail@gotmail.com
    nextemailaddy@gaggle.com
    andthenextone@wahoo.ca

message.ini
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut at pharetra enim. In et scelerisque erat. Mauris ac velit lorem. Aenean a mauris quam. Aenean sit amet maximus ante. In fermentum efficitur scelerisque. Maecenas facilisis maximus ipsum. Suspendisse porttitor justo nec ornare ullamcorper. Aliquam blandit arcu arcu, id mollis neque blandit et. Phasellus et elementum ante. Suspendisse vitae vestibulum ligula.

    Quisque viverra dignissim dui, id convallis tortor condimentum quis. Sed nec mi sit amet tortor condimentum aliquam. Morbi velit nisl, volutpat in iaculis vitae, mattis eu sem. Fusce laoreet, diam eget dictum fringilla, lorem nisl lacinia lacus, ac varius lacus augue sed sapien. Morbi ac dui porta, sollicitudin metus et, rutrum magna. Integer sit amet nunc ultricies, fringilla augue non, auctor augue. Vivamus nec imperdiet diam, sit amet placerat sem. Nullam odio dui, luctus sit amet nunc in, pulvinar pulvinar orci. Nam nec dignissim ligula. Curabitur eget nulla at nunc dapibus lobortis non eu augue. Maecenas sed dolor tortor.



WIP:
profiles for different settings.
no attachment mode.

NOTES:
RAD via Google Collab AI, OpenAI ChatGPT and myself doing the final tuning.
