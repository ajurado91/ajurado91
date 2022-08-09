# AT16-POST-WORDPRESS
#

Preconditions:
- Install XAMPP, WAMP, LAMP or MAMP
- Install Wordpress
- Create file .env with the next variables:
    - URI_TOKEN="http://localhost/wordpress/wp-json/api/v1/token"
    - USER_NAME="NAME_WORPRESS"
    - PASSWORD="PASSWORD_WORDPRESS"
    - URL="http://localhost/wordpress/wp-json/wp/v2/posts"

For windows users:
- Open the Powershell terminal, and enter the next commands:
    - Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    - irm get.scoop.sh | iex
    - scoop install allure

Steps:
- Pull project https://github.com/AT16-APITESTING-G2/AT16-POST-WORDPRESS.git
- Move to "develop" branch
- Install requirements.txt, for this use the command: pip install -r requirements.txt
- Move to /test folder to run the test cases
- Execute the commands:
    - For a general report (all tags included):
        - py.test --alluredir=general_report .
        - allure serve .\general_report

    - For a specific report:
        - pytest . -sq --alluredir=(tag)_testing --allure-epics (tag)_testing
        - allure serve ./(tag)_testing
            * (replace (tag) for one of the tags used in the test, this can be: acceptance_testing, smoke_testing, regression_testing, sanity_testing, negative_testing, security_testing, endtoend_testing, blackbox_testing, functional_testing)

