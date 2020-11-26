from setuptools import setup, find_packages

setup(
    name="tljh-voila-gallery",
    version="0.0.1",
    entry_points={
        "tljh": ["tljh_voila_gallery = tljh_voila_gallery"],
        "console_scripts": [
            "build-gallery-images = tljh_voila_gallery.build_images:main",
            "install-builder-units = tljh_voila_gallery.install_builder_units:main"
        ]
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # These get installed into the hub environment
        'dockerspawner',
        'jupyter-repo2docker @ git+https://github.com/hndgzkn/repo2docker',
        'binderhub',
        'nullauthenticator'
    ]
)
