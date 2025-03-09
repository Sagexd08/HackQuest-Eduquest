from flask import Blueprint

# Create blueprint
ai_bp = Blueprint('ai', __name__)

# Import views after blueprint creation
from api import routes