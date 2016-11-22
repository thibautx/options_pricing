import os

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
SQLALCHEMY_DATABASE_URI = "postgresql://localhost/database"
SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
# Use a secure, unique and absolutely secret key for signing the data.
CSRF_ENABLED = True
CSRF_SESSION_KEY = "8a7474974efcf76896aa84eea9cbe016bbc08828"

# Secret key for signing cookies
SECRET_KEY = '47e585de7f22984d5ee291c2f31412384bfc32d0'
FLASH_MESSAGES = True


# Flask-Login
# https://flask-login.readthedocs.org/en/latest/#protecting-views
LOGIN_DISABLED = False

# Flask-Security
# http://pythonhosted.org/Flask-Security/configuration.html
SECURITY_PASSWORD_SALT = "abc"
SECURITY_PASSWORD_HASH = "bcrypt"  # requires py-bcrypt
SECURITY_EMAIL_SENDER = "support@example.com"
SECURITY_CONFIRMABLE = True
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True
SECURITY_CONFIRM_SALT = "570be5f24e690ce5af208244f3e539a93b6e4f05"
SECURITY_REMEMBER_SALT = "de154140385c591ea771dcb3b33f374383e6ea47"
SECURITY_DEFAULT_REMEMBER_ME = True
# SECURITY_CHANGE_URL = ''

# Flask-Babel
# http://pythonhosted.org/Flask-Babel/
BABEL_DEFAULT_LOCALE = "en"
BABEL_DEFAULT_TIMEZONE = "UTC"

# Flask-Mail
# http://pythonhosted.org/Flask-Mail/
SERVER_EMAIL = 'Flask-SocialBlueprint <support@example.com>'

# Flask-SocialBlueprint
# https://github.com/wooyek/flask-social-blueprint
SOCIAL_BLUEPRINT = {
    # https://developers.facebook.com/apps/
    "flask_social_blueprint.providers.Facebook": {
        # App ID
        'consumer_key': '1736167959983448',
        # App Secret
        'consumer_secret': '3f28ce9bc466f2b295876b0d857f9bd2'
    },
}
