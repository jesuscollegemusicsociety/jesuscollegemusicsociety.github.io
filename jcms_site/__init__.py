from flask import Flask, send_from_directory, render_template
from flask_assets import Environment
from jinja_markdown import MarkdownExtension
from pathlib import Path
import yaml

from .images import load_images

root_dir = Path(__file__).parent.resolve()

app = Flask(__name__)
app.jinja_env.add_extension(MarkdownExtension)
app.jinja_loader.searchpath.append(str(root_dir / "text"))
app.config.update(
    FREEZER_DESTINATION="../build",
)

assets = Environment(app)
assets.from_yaml("assets.yml")

data = {}
for path in root_dir.glob("data/**/*.yml"):
    with path.open() as file:
        data[str(path.relative_to(root_dir / "data"))] = yaml.safe_load(file)

app.jinja_env.globals["data"] = data

load_images(app)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(root_dir / "static", "favicon/favicon.ico")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/termcard/")
def termcard():
    return render_template("termcard.html")


@app.route("/calendar/")
def calendar():
    return render_template("calendar.html")


@app.route("/concert-archives/")
def concert_archives():
    return render_template("concert-archives.html")


@app.route("/committee/")
def committee():
    return render_template("committee.html")


@app.route("/ensembles-events/")
def ensembles_events():
    return render_template("ensembles-events.html")


@app.route("/hire/")
def hire():
    return render_template("hire.html")


@app.route("/hire/catalogue/")
def catalogue():
    return render_template("catalogue.html")


@app.route("/hire/inventory/")
def inventory():
    return render_template("inventory.html")
