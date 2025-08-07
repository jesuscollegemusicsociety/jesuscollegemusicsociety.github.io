from flask_frozen import Freezer
from jcms_site import app

freezer = Freezer(app)
freezer.freeze()
