# The JCMS Website

Hello, dear future Webmaster. Herein lies the JCMS website, as designed by Shrey S. (Jesus, 2020)
and implemented by Jeremy S. (Jesus, 2023). Read on for an outline of what you need to know to make
edits to the website.

The website is hosted on `github.com`. You should have access via the webmaster email. All changes
to the website will need to be made from `github.com`. Any files uploaded to this site are
publically accessible, even if they are not included on the website.

If you encounter any problems **which this document does not resolve**, contact Jeremy S. on 
whatever contact details he left with the Office of the Webmaster, or another person with web
development experience.

## Basic edits

Provided you read this section carefully, you will be able to make these changes regardless of
level of expertise. Make sure you read the whole section before attempting any changes.

If after making and committing a change, the website does not change, that means the build failed,
and you (or one of your predecessors) did something wrong. Once you fix the error, it will build.

### Adding, changing and removing images

All images live in the folder `jcms_site / images`. To add an image to the website:

1. Upload the image to this folder. You can do this with the "Add file" button.
2. Specify where the image goes:
   * If it is to be on the landing page, go to `jcms_site / data / home-carousel.yml`. Add an entry
     of the form
     ```yaml
     - file: [image name].webp
       alt: [altenative text for screen readers]
     ```
   * If it is to be on the Committee page, go to `jcms_site / data / committee.yml`. Add an entry
     of the form
     ```yaml
     - name: [name]
       role: [role]
       email: [jcms email]
       photo: [image name].webp
     ```
   * For other locations, see [Advanced Edits](#advanced-edits)
   
   Note that regardless of which image format you upload (which should in general be `.png` or
   `.jpeg`), you should replace the extension with `.webp`.

To change an image:

1. Find the image in `jcms_site / images`.
2. Delete the image.
3. Upload the replacement image, **keeping the file name the same**. The file extension (e.g.
   `.png` or `.jpeg`) may be different.

Note that:

* The termcard is the image `termcard.png` (or another extension).
* The JCMS logo is the image `jcms-logo.avif`.
* The Facebook and Instagram logos are `facebook-logo.png` and `instagram-logo.png`. Do not change
  these without first consulting the Meta brand policy.

To delete an image:

1. Find the image in `jcms_site / images`.
2. Delete the image.
3. Find any entries (see above) where the image is used and remove them.

If you miss step 3, or delete one of the images specifically named above, the website may not
build correctly.

## Changing text on the website

The text for the text-heavy pages (listed below) is stored in the `jcms_site / text` in Markdown format. You can find various tutorials and editors for Markdown on the internet.

* About Us page: `about.md`
* Concert Archives page: `concert-archives.md`
* Ensembles and Events page: `ensembles-events.md`
* Hire page: `hire.md`

## Advanced edits

The changes in this section will require varying levels of expertise, and are only briefly
outlined. Attempt at your own risk.

The website is implemented as a Flask app, using Frozen-Flask to generate static files. These
static files are hosted on GitHub pages, and the build step is automated using GitHub actions. The
following libraries are already included:

* `flask-assets` for asset management
* `jinja-markdown` for using Markdown in Jinja
* `pillow` for image management
* `flickity` for image carousels
* `htmx` for SPA navigation and basic scripting needs

Try to maintain a small set of libraries (particularly JS libraries): this will ensure the website
stays fast and light.

You may find it useful to have a local development environment; this can be done using the Python
package manager `uv`. Once you have cloned the repo locally and install `uv`, a development server
can be run using

```shell
$ uv run flask --app jcms_site run --debug
```

The static site can be generated using

```shell
$ uv run build.py
```

Both steps will need to rescale every image used on the website. This will take a while: be
patient.

### The nav bar

The links found on the nav bar are defined in `jcms_site / data / sitemap.yml`.

### Adding or removing pages

All pages are defined in `jcms_site / __init__.py`. Read a Flask tutorial before changing this.

The content of pages is defined in `jcms_site / templates`. Read a Jinja tutorial before changing
these.

### Changing styling

All stylesheets can be found in `jcms_site / static / src / css`. Read a CSS tutorial before
changing these. If you add a new file, make sure it is added to `assets.yml` (at the project root)
or it won't be included.

### Adding scripts

All scripts can be found in `jcms_site / static / src / js`. Read a JS tutorial before changing
these.If you add a new file, make sure it is added to `assets.yml` (at the project root) or it
won't be included.
