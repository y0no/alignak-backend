#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main
"""
from alignak_backend.app import app, manifest, settings


def main():
    """
    Main function
    """
    try:
        print("--------------------------------------------------------------------------------")
        print("%s, listening on %s:%d" % (
            manifest['name'], app.config.get('HOST', '127.0.0.1'), app.config.get('PORT', 8090)
        ))
        print("--------------------------------------------------------------------------------")
        app.run(
            host=settings.get('HOST', '127.0.0.1'),
            port=settings.get('PORT', 5000),
            debug=settings.get('DEBUG', False)
        )
    except Exception as e:
        print("Application run failed, exception: %s / %s" % (type(e), str(e)))

if __name__ == "__main__":  # pragma: no cover
    main()
