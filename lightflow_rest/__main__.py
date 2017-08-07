

def main(args):
    """ Main entry point for the extension. """
    from lightflow_rest.service import app
    app.run()


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
