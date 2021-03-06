Hub Storage client library
==========================

.. note:: This module is experimental and its API may change without previous
   notice.

This is the HubStorage client library, which contains:

* basic client api (hubstorage.Client)
* a simple command line tool (hubstorage.tool)
* a tool to convert log files from log.json API format to HubStorage format
  (hubstorage.shlog2jl)

Requirements
------------

* requests: http://pypi.python.org/pypi/requests

Basic API
---------

Example creating a new job::

    >> hs = HSClient(auth=apikey)
    >> job = hs.new_job(projectid='1111111', spider='foo')
    >> job.key
    '1111111/1/1'

    >> job.metadata['state']
    'pending'

    >> job.update(state='running')
    >> job.metadata['state']
    'running'

    >> job.logs.info('Job started')
    >> job.items.write({'title': 'lorem ipsum...'})

    ...

Example getting job data later::

    >> job = hs.get_job('1111111/1/1')
    >> job.metadata['state']
    'running'

    >> job.logs.get().next()
    {'message': 'Job started', 'time': 123456789, 'level': 20}

    >> job.items.get().next()
    {'title': 'lorem ipsum...'}


Basic API (old)
---------------

Example for writing::

    from hubstorage import Client
    client = Client()
    with client.open_item_writer('items/1/2/3') as writer:
        for item in items:
            write.write_item(item)

Example for reading::

    from hubstorage import Client
    client = Client()
    for item in client.iter_items('items/1/2/3'):
        print item

Command line tool
-----------------

Some example usage:

To dump the items of a job in jsonlines format::

    python -m hubstorage.tool --dump items/53/34/7

To upload a jsonlines file into a job::

    cat items.jl | python -m hubstorage.tool --load items/53/34/7

To upload a jsonlines file into a job using `pipe viewer`_ to monitor progress
and throughput::

    pv -l items.jl | python -m hubstorage.tool --load items/53/34/7

.. _pipe viewer: http://www.ivarch.com/programs/pv.shtml
