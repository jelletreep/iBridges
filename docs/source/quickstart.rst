Quick Start Guide
=================


Installation
------------

iBridges requires Python version 3.8 or higher. You can install iBridges with pip:

.. code:: bash

    pip install ibridges


Getting your iRODS environment file
-----------------------------------

To connect to an iRODS server you need an iRODS environment file (`iRODS_nevironment.json`).
You can obtain this by asking your local iRODS administrator. An example of an environment file:

.. code:: json

    {
        "iRODS_host": "provider.yoda",
        "iRODS_port": 8247,
        "iRODS_user_name": "technicaladmin",
        "iRODS_home": "/tempZone/home/rods",
        "iRODS_cwd": "/tempZone/home/rods",
        "iRODS_zone_name": "tempZone",
        "iRODS_client_server_negotiation": "request_server_negotiation",
        "iRODS_client_server_policy": "CS_NEG_REQUIRE",
        "iRODS_default_hash_scheme": "SHA256",
        "iRODS_default_resource": "iRODSResc",
        "iRODS_encryption_algorithm": "AES-256-CBC",
        "iRODS_encryption_key_size": 32,
        "iRODS_encryption_num_hash_rounds": 16,
        "iRODS_encryption_salt_size": 8,
        "iRODS_ssl_verify_server": "none"
    }

Normally this file is stored in `~/.iRODS/iRODS_environment.json`. It is recommended to store it in the default location,
but if needed (if you need access to more than one iRODS instance for example) you can also store it elsewhere. Simply
replace that path in this quick start guide with the path you have chosen.


Connecting to your iRODS server
-------------------------------

To connect to your iRODS server, we will create a session. The session is the central object in the iBridges library;
almost all functionality is enabled with this connection to your server. Generally you will create a session,
perform your data operations, and then delete/close the session. To create a new session, open Python:

.. code:: python

    from ibridges import Session
    from pathlib import Path

    session = Session(iRODS_env=Path("~/.iRODS/iRODS_environment.json").expanduser(), password="mypassword")


Upload data
-----------

You can easily upload your data with the previously created session:

.. code:: python

    from ibridges import upload

    upload(session, "/your/local/path", "/iRODS/path")

This upload function can upload both directories (collections in iRODS) and files (data objects in iRODS)


Add metadata
------------

One of the powerful features of iRODS is its ability to store metadata with your data in a consistent manner.
Let's add some metadata to a collection or data object:

.. code:: python

    from ibridges import MetaData, get_collection

    collection = get_collection("/iRODS/path")
    meta = MetaData(collection)
    meta.add("some_key", "some_value", "some_units")


Download data
-------------

Naturally, we also want to download the data back to our local machine. This is done with the download function:

.. code:: python

    from ibridges import download

    download(session, "/iRODS/path", "/other/local/path")


Closing the session
-------------------
When you are done with your session, you should generally close it:

.. code:: python

    session.close()

