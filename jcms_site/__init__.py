from flask import Flask, send_from_directory, render_template, url_for
from jinja_markdown import MarkdownExtension
from pathlib import Path
import yaml

root_dir = Path(__file__).parent.resolve()

app = Flask(__name__)
app.jinja_env.add_extension(MarkdownExtension)
app.jinja_loader.searchpath.append(str(root_dir / "text"))
app.config.update(
    FREEZER_DESTINATION="../build",
)


data = {}
for path in root_dir.glob("data/**/*.yml"):
    with path.open() as file:
        data[str(path.relative_to(root_dir / "data"))] = yaml.safe_load(file)


@app.context_processor
def data_processor():
    return {"data": data}


@app.context_processor
def photo_processor():
    def photo(file):
        return url_for("static", filename="photos/" + file)

    return {"photo": photo}


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


@app.route("/ensembles/")
def ensembles():
    return render_template("ensembles.html")


@app.route("/hire/")
def hire():
    return render_template("hire.html")

