.. _resource-logcheckresult:

logcheckresult
===================

.. image:: ../_static/logcheckresult.png


.. csv-table::
   :header: "Parameter", "Type", "Required", "Default", "Data relation"

   "last_state", "string", "", "OK", ""
   "latency", "float", "", "0.0", ""
   "state_changed", "boolean", "", "False", ""
   "**last_state_type**", "**string**", "**True**", "****", ""
   "**service**", "**objectid**", "**True**", "****", ":ref:`service <resource-service>`"
   "output", "string", "", "", ""
   "execution_time", "float", "", "0.0", ""
   "service_name", "string", "", "", ""
   "acknowledged", "boolean", "", "False", ""
   "**state**", "**string**", "**True**", "****", ""
   "last_check", "integer", "", "None", ""
   "**state_type**", "**string**", "**True**", "****", ""
   "long_output", "string", "", "", ""
   "**host**", "**objectid**", "**True**", "****", ":ref:`host <resource-host>`"
   "host_name", "string", "", "", ""
   "last_state_id", "integer", "", "0", ""
   "state_id", "integer", "", "0", ""
   "_sub_realm", "boolean", "", "False", ""
   "_users_read", "list of objectid", "", "", ":ref:`user <resource-user>`"
   "perf_data", "string", "", "", ""
   "**_realm**", "**objectid**", "**True**", "****", ":ref:`realm <resource-realm>`"

