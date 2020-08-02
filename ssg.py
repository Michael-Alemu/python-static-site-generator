import typer
from ssg.site import Site

def main(source = "content", dest="dest"):
    config= {
        "source":"source",
        "dest":"dest"
    }
    site = Site(**config)
    print('calling build')
    site.build()



typer.run(main)

