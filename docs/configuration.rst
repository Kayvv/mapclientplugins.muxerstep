.. _mcp-muxer-configuration:

Configuration
-------------

Some care must be taken when configuring this step because it programmatically manipulates the step ports.
Because of this we **must** configure the *Mux type* parameter **and** *Number of inputs* parameter **before** we make connections to the step.
Existing connections will not be maintained if either of these two parameters are modified after the fact, resulting in the need to delete and redo connections involving the step.

The *Mux type* parameter should be a port type, for example: 'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'.
The *Number of inputs* parameter should be set to the number of inputs to mux together.

.. _fig-mcp-muxer-configure-dialog:

.. figure:: _images/step-configuration-dialog.png
   :alt: Step configure dialog

   *Muxer* step configuration dialog.

The step will accept either single inputs or list of inputs for each port.
All list inputs will be expanded on output so that the resulting output will be a single level list.