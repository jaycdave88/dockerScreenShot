# Docker Screen shot
> *Purpose*: To create a self contained ecosystem around the ability to take a public URL and create a screen shot, which then would be sent over SMTP to a specified individual. 

_Prerequisites_:
* If you will be sending messages from gmail, please configure your gmail account to, `Allow less secure apps: ON` Information can be found here: https://support.google.com/accounts/answer/6010255?hl=en

_Run commands_:

1. The code below will allow you to set `ENV Variables` into your Docker Container along with providing the **REQUIRED** fields in the format below:

    ```docker run -d --env FROM_ADDRESS=[JOHN@SMITH.COM] --env EMAIL_PASSWORD=[PASSWORD_HERE] --env SUBJECT=["This is an example of a subject"] --env TO_ADDRESS=[JANE@SMITH.COM] --env SAVE_LOCATION=[FILE_NAME_AND_PATH_TO_STORE_IMAGE] --env SMTP_ADDRESS=smtp.gmail.com:587 --name [PROVIDE_CONTAINER_NAME_ALIAS] jaycdave88/dockerscreenshot```

2. Once everything has been downloaded, run the following command:

    ```docker container exec [PROVIDE_CONTAINER_NAME_ALIAS_WHICH_WAS_DEFINED_ABOVE_IN_STEP_1] /usr/bin/xvfb-run -a /usr/bin/wkhtmltoimage --javascript-delay 20000 "[LINK_TO_PUBLIC_URL]" [FILE_NAME_AND_PATH_TO_STORE_IMAGE_PREVIOUSLY_SET_IN_STEP_1]; docker container exec [PROVIDE_CONTAINER_NAME_ALIAS_WHICH_WAS_DEFINED_ABOVE_IN_STEP_1] python3 /usr/bin/dd-email.py```
    
(***NOTE***: All items noted above surrounded with `[ ]` will need to be replaced with appropriate fields.)

(P.S. Make sure you check your `Spam` folder for your email - incase the message was sent there)

_Enhancements_: 

* The ability to send emails to multiple recipients. In order to achieve this, just update the `TO_ADDRESS` with the format below:

    ```TO_ADDRESS="JANE@SMITH.COM, JOE@SMITH.COM, "MATT@SMITH.COM" ```