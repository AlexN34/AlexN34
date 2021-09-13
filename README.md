# Blog site

## Building

- use `poetry run <command>` to work in virtualenv
- `pelican content` to generate to `./output`
- `pelican --listen` to test locally

# Push

- See makefile:github for shortcut - when make is available simply `make github`
- Otherwise:

``` shell
poetry run ghp-import -m "Generate Pelican site" -b master ./output --no-jekyll
git push origin master
```

## Plugins / themes

- need relative references on local system; clone to paths specified in `pelicanconf.py`
- pdf - need imagemagick wand as dependency - this is a pain on windows, don't compile on windows if needed

