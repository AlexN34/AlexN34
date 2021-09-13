# Blog site

## Building

- use `poetry run <command>` to work in virtualenv
- `pelican content` to generate to `./output`
- `pelican --listen` to test locally

## Plugins / themes

- need relative references on local system; clone to paths specified in `pelicanconf.py`
- pdf - need imagemagick wand as dependency - this is a pain on windows, don't compile on windows if needed