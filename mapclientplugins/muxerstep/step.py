"""
MAP Client Plugin Step
"""
import json

from PySide6 import QtGui

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.muxerstep.configuredialog import ConfigureDialog


class MuxerStep(WorkflowStepMountPoint):
    """
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    """

    def __init__(self, location):
        super(MuxerStep, self).__init__('Muxer', location)
        self._configured = False  # A step cannot be executed until it has been configured.
        self._category = 'Utility'
        # Add any other initialisation code here:
        self._icon = QtGui.QImage(':/muxerstep/images/utility.png')
        self._skeleton_output_triple = \
            ['http://physiomeproject.org/workflow/1.0/rdf-schema#port',
             'http://physiomeproject.org/workflow/1.0/rdf-schema#provides-list-of',
             'XXXX']
        self._skeleton_input_triple_individual = \
            ['http://physiomeproject.org/workflow/1.0/rdf-schema#port',
             'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
             'XXXX']
        self._skeleton_input_triple_list = \
            ['http://physiomeproject.org/workflow/1.0/rdf-schema#port',
             'http://physiomeproject.org/workflow/1.0/rdf-schema#uses-list-of',
             'XXXX']

        # Ports:
        self.addPort(tuple(self._skeleton_output_triple))
        self.addPort([tuple(self._skeleton_input_triple_individual),
                      tuple(self._skeleton_input_triple_list)])

        # Port data:
        self._data_store = [None]
        # Config:
        self._config = {
            'identifier': '',
            'port_type': '',
            'input_port_count': 1
        }

    def _process_config(self):
        self._ports.clear()

        port_type = self._config['port_type']
        port_count = self._config['input_port_count']

        self._data_store = [None] * port_count
        output_port_triple = self._skeleton_output_triple
        output_port_triple[2] = port_type
        self.addPort(tuple(output_port_triple))
        input_port_triple_individual = self._skeleton_input_triple_individual
        input_port_triple_list = self._skeleton_input_triple_list
        input_port_triple_individual[2] = port_type
        input_port_triple_list[2] = port_type
        for i in range(port_count):
            self.addPort([tuple(input_port_triple_individual), tuple(input_port_triple_list)])

    def execute(self):
        """
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        """
        # Put your execute step code here before calling the '_doneExecution' method.
        self._doneExecution()

    def getPortData(self, index):
        """
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.
        """
        output = []
        for data in self._data_store:
            if data is not None:
                if isinstance(data, list):
                    output.extend(data)
                else:
                    output.append(data)

        return output

    def setPortData(self, index, dataIn):
        """
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.

        :param index: Index of the port to return.
        :param dataIn: The data to set for the port at the given index.
        """
        # Offset the index to account for the output port which is the first port.
        self._data_store[index - 1] = dataIn

    def configure(self):
        """
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        """
        dlg = ConfigureDialog(self._main_window)
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()
            self._process_config()

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        """
        The identifier is a string that must be unique within a workflow.
        """
        return self._config['identifier']

    def setIdentifier(self, identifier):
        """
        The framework will set the identifier for this step when it is loaded.
        """
        self._config['identifier'] = identifier

    def serialize(self):
        """
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        """
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        """
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.

        :param string: JSON representation of the configuration in a string.
        """
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()
        self._process_config()
