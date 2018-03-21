import sys
from datetime import datetime

TEMPLATE = """

Title: {title}
Date: {year}-{month}-{day} {hour}:{minute:02d}
Tags: 
Slug: {slug}
Category: 
Author: Alex Nguyen
Summary: 
save_as: {slug}.html

{title}
{hashes}

"""


def make_entry(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    file_name = "{}_{:0>2}_{:0>2}_{}".format(
        today.year, today.month, today.day, slug)
    f_create = f"../content/articles/{slug}.md"
    t = TEMPLATE.strip().format(title=title,
                                hashes='#' * len(title),
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug,
                                file_name=file_name)
    with open(f_create, 'w') as w:
        w.write(t)
    print("File created -> " + f_create)


if __name__ == '__main__':

    if len(sys.argv) > 1:
        make_entry(sys.argv[1])
    else:
        print( "No title given")
