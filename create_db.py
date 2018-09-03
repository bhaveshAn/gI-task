import argparse
import getpass
import re
import sys

from flask_migrate import stamp

from app import current_app
from app.models import db

if __name__ == "__main__":
    with current_app.app_context():
        db.create_all()
        stamp()
