# -*- coding: utf-8 -*-
import sys

from bookStore import app, db


def main():
    try:
        args = sys.argv
        job_name = args.pop(1)
        mod_name = 'bookStore.jobs.%s' % job_name
        app.ready()

        mod = __import__(mod_name, fromlist=['*'])
        mod.run(*sys.argv[1:])
        return 0
    except:
        raise
    finally:
        db.session.remove()


if __name__ == '__main__':
    with app.app_context():
        sys.exit(main())
