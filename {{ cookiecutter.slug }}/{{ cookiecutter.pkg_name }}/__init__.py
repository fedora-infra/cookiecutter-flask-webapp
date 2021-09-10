# Set the version
try:
    import importlib.metadata

    __version__ = importlib.metadata.version("{{ cookiecutter.pkg_name }}")
except ImportError:
    try:
        import pkg_resources

        try:
            __version__ = pkg_resources.get_distribution(
                "{{ cookiecutter.pkg_name }}"
            ).version
        except pkg_resources.DistributionNotFound:
            __version__ = None
    except ImportError:
        __version__ = None
