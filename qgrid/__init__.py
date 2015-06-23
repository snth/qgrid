from .grid import show_grid, SlickGrid      # noqa


def nbinstall(user=True, overwrite=False):
    """
    """
    # Lazy imports so we don't pollute the namespace.
    import os
    from IPython.html.nbextensions import install_nbextension
    from IPython import version_info

    qgridjs_path = os.path.join(
        os.path.dirname(__file__),
        'qgridjs',
    )

    install_nbextension(
        qgridjs_path,
        overwrite=overwrite,
        symlink=False,
        verbose=0,
        **({'user': user} if version_info>=(3, 0, 0, '') else {})
    )
