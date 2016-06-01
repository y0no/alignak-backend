#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Resource information of host
"""


def get_name():
    """
    Get name of this resource

    :return: name of this resource
    :rtype: str
    """
    return 'host'


def get_schema():
    """
    Schema structure of this resource

    :return: schema dictionary
    :rtype: dict
    """
    return {
        # 'allow_unknown': True,
        'schema': {
            # 'uuid': {
                # 'type': 'string',
                # 'required': True,
                # 'empty': False,
                # 'unique': True
            # },

            'imported_from': {
                'type': 'string',
                'ui': {
                    'title': 'Import source',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': ''
            },
            'name': {
                'type': 'string',
                'ui': {
                    'title': 'Host name',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'required': True,
                'empty': False,
                'unique': True,
                'regex': '^[^`~!$%^&*"|\'<>?,()=]+$',
                'dependencies': ['check_command']
            },
            'definition_order': {
                'type': 'integer',
                'ui': {
                    'title': 'Definition order',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': 100
            },
            'alias': {
                'type': 'string',
                'ui': {
                    'title': 'Alias',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': ''
            },
            'display_name': {
                'type': 'string',
                'ui': {
                    'title': 'Display name',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': ''
            },
            'address': {
                'type': 'string',
                'ui': {
                    'title': 'Adress',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': ''
            },
            'parents': {
                'type': 'list',
                'ui': {
                    'title': 'Parents',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': "link"
                },
                'schema': {
                    'type': 'objectid',
                    'data_relation': {
                        'resource': 'host',
                        'embeddable': True,
                    }
                },
            },
            'hostgroups': {
                'type': 'list',
                'ui': {
                    'title': 'Hosts groups',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': "link"
                },
                'schema': {
                    'type': 'objectid',
                    'data_relation': {
                        'resource': 'hostgroup',
                        'embeddable': True,
                    }
                },
            },
            'check_command': {
                'type': 'objectid',
                'ui': {
                    'title': 'Check command',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': "link"
                },
                'data_relation': {
                    'resource': 'command',
                    'embeddable': True
                }
            },
            'check_command_args': {
                'type': 'string',
                'ui': {
                    'title': 'Check command arguments',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': ''
            },
            'initial_state': {
                'type': 'string',
                'ui': {
                    'title': 'Initial state',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'minlength': 1,
                'maxlength': 1,
                'default': 'u',
                'allowed': ["o", "d", "u"]
            },
            'max_check_attempts': {
                'type': 'integer',
                'ui': {
                    'title': 'Max check attempts',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': 1
            },
            'check_interval': {
                'type': 'integer',
                'ui': {
                    'title': 'Check interval',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': 5
            },
            'retry_interval': {
                'type': 'integer',
                'ui': {
                    'title': 'Retry interval',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': 0
            },
            'active_checks_enabled': {
                'type': 'boolean',
                'ui': {
                    'title': 'Active checks enabled',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': True
            },
            'passive_checks_enabled': {
                'type': 'boolean',
                'ui': {
                    'title': 'Passive checks enabled',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': True
            },
            'check_period': {
                'type': 'objectid',
                'ui': {
                    'title': 'Check period',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': "link"
                },
                'data_relation': {
                    'resource': 'timeperiod',
                    'embeddable': True
                }
            },
            'check_freshness': {
                'type': 'boolean',
                'ui': {
                    'title': 'Check freshness',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': False
            },
            'freshness_threshold': {
                'type': 'integer',
                'ui': {
                    'title': 'Freshness threshold',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': 0
            },
            'event_handler': {
                'type': 'objectid',
                'ui': {
                    'title': 'Event handler',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'data_relation': {
                    'resource': 'command',
                    'embeddable': True
                },
                'nullable': True
            },
            'event_handler_enabled': {
                'type': 'boolean',
                'ui': {
                    'title': 'Event handler enabled',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': False
            },
            'low_flap_threshold': {
                'type': 'integer',
                'ui': {
                    'title': 'Low flapping threshold',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': 25
            },
            'high_flap_threshold': {
                'type': 'integer',
                'ui': {
                    'title': 'High flapping threshold',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': 50
            },
            'flap_detection_enabled': {
                'type': 'boolean',
                'ui': {
                    'title': 'Flapping detection enabled',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': True
            },
            'flap_detection_options': {
                'type': 'list',
                'ui': {
                    'title': 'Flapping detection options',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': {
                        'list_type': "multichoices",
                        'list_allowed': {
                            u"d": u"Down",
                            u"o": u"Up",
                            u"u": u"Unreachable"
                        }
                    }
                },
                'default': ['o', 'd', 'u'],
                'allowed': ['o', 'd', 'u']
            },
            'process_perf_data': {
                'type': 'boolean',
                'ui': {
                    'title': 'Process performance data',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': True
            },
            'retain_status_information': {
                'type': 'boolean',
                'ui': {
                    'title': 'Retain status information',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': True
            },
            'retain_nonstatus_information': {
                'type': 'boolean',
                'ui': {
                    'title': 'Retain non status information',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': True
            },
            'contacts': {
                'type': 'list',
                'ui': {
                    'title': 'Contacts',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': "link"
                },
                'schema': {
                    'type': 'objectid',
                    'data_relation': {
                        'resource': 'contact',
                        'embeddable': True,
                    }
                },
            },
            'contact_groups': {
                'type': 'list',
                'ui': {
                    'title': 'Contacts group(s)',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': "link"
                },
                'schema': {
                    'type': 'objectid',
                    'data_relation': {
                        'resource': 'contactgroup',
                        'embeddable': True,
                    }
                },
            },
            'notification_interval': {
                'type': 'integer',
                'ui': {
                    'title': 'Notification interval',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': 60
            },
            'first_notification_delay': {
                'type': 'integer',
                'ui': {
                    'title': 'First notification delay',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': 0
            },
            'notification_period': {
                'type': 'objectid',
                'ui': {
                    'title': 'Notification period',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': "link"
                },
                'data_relation': {
                    'resource': 'timeperiod',
                    'embeddable': True
                }
            },
            'notification_options': {
                'type': 'list',
                'ui': {
                    'title': 'Notification options',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': {
                        'list_type': "multichoices",
                        'list_allowed': {
                            u"d": u"Send notifications on Down state",
                            u"r": u"Send notifications on recoveries",
                            u"u": u"Send notifications on Unreachable state",
                            u"f": u"Send notifications on flapping start/stop",
                            u"s": u"Send notifications on scheduled downtime start/stop",
                            u"n": u"Do not send notifications"
                        }
                    }
                },
                'default': ['d', 'u', 'r', 'f', 's'],
                'allowed': ['d', 'u', 'r', 'f', 's', 'n']
            },
            'notifications_enabled': {
                'type': 'boolean',
                'ui': {
                    'title': 'Notifications enabled',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': True
            },
            'stalking_options': {
                'type': 'list',
                'ui': {
                    'title': 'Stalking options',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': {
                        'list_type': "multichoices",
                        'list_allowed': {
                            u"d": u"Down",
                            u"o": u"Up",
                            u"u": u"Unreachable"
                        }
                    }
                },
                'default': [],
                'allowed': ['o', 'd', 'u']
            },
            'notes': {
                'type': 'string',
                'ui': {
                    'title': 'Notes',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': ''
            },
            'notes_url': {
                'type': 'string',
                'ui': {
                    'title': 'Notes URL',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': ''
            },
            'action_url': {
                'type': 'string',
                'ui': {
                    'title': 'Action URL',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': ''
            },
            'icon_image': {
                'type': 'string',
                'ui': {
                    'title': 'Icon image',
                    'visible': False,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': ''
            },
            'icon_image_alt': {
                'type': 'string',
                'ui': {
                    'title': 'Icon image alt',
                    'visible': False,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': ''
            },
            'icon_set': {
                'type': 'string',
                'ui': {
                    'title': 'Icon set',
                    'visible': False,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': ''
            },
            'vrml_image': {
                'type': 'string',
                'ui': {
                    'title': 'VRML image',
                    'visible': False,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': ''
            },
            'statusmap_image': {
                'type': 'string',
                'ui': {
                    'title': 'Status map image',
                    'visible': False,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': ''
            },
            '2d_coords': {
                'type': 'string',
                'ui': {
                    'title': '2D coordinates',
                    'visible': False,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': ''
            },
            '3d_coords': {
                'type': 'string',
                'ui': {
                    'title': '3D coordinates',
                    'visible': False,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': ''
            },
            'failure_prediction_enabled': {
                'type': 'boolean',
                'ui': {
                    'title': 'Failure prediction enabled',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': False
            },
            'realm': {
                'type': 'objectid',
                'ui': {
                    'title': 'Realm',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': "link"
                },
                'data_relation': {
                    'resource': 'realm',
                    'embeddable': True
                },
                'required': True,
            },
            'poller_tag': {
                'type': 'string',
                'ui': {
                    'title': 'Poller tag',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': 'None'
            },
            'reactionner_tag': {
                'type': 'string',
                'ui': {
                    'title': 'Reactionner tag',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': 'None'
            },
            'resultmodulations': {
                'type': 'list',
                'ui': {
                    'title': 'Result modulations',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': []
            },
            'business_impact_modulations': {
                'type': 'list',
                'ui': {
                    'title': 'Business impact modulations',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': []
            },
            'escalations': {
                'type': 'list',
                'ui': {
                    'title': 'Escalations',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': [],
                'schema': {
                    'type': 'objectid',
                    'data_relation': {
                        'resource': 'escalation',
                        'embeddable': True,
                    }
                },
            },
            'maintenance_period': {
                'type': 'objectid',
                'ui': {
                    'title': 'Maintenance period',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': "link"
                },
                'data_relation': {
                    'resource': 'timeperiod',
                    'embeddable': True
                },
                'nullable': True
            },
            'time_to_orphanage': {
                'type': 'integer',
                'ui': {
                    'title': 'Time to orphanage',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': 300
            },
            'service_overrides': {
                'type': 'list',
                'ui': {
                    'title': 'Service overrides',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': []
            },
            'service_excludes': {
                'type': 'list',
                'ui': {
                    'title': 'Service excludes',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': []
            },
            'service_includes': {
                'type': 'list',
                'ui': {
                    'title': 'Service includes',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': []
            },
            'labels': {
                'type': 'list',
                'ui': {
                    'title': 'Business rules labels',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': []
            },
            'business_rule_output_template': {
                'type': 'string',
                'ui': {
                    'title': 'Business rules output template',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': ''
            },
            'business_rule_smart_notifications': {
                'type': 'boolean',
                'ui': {
                    'title': 'Business rules smart notifications',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': False
            },
            'business_rule_downtime_as_ack': {
                'type': 'boolean',
                'ui': {
                    'title': 'Business rules downtime as ack',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': False
            },
            'business_rule_host_notification_options': {
                'type': 'list',
                'ui': {
                    'title': 'Business rules host notification options',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': ['d', 'u', 'r', 'f', 's'],
                'allowed': ['d', 'u', 'r', 'f', 's', 'n']
            },
            'business_rule_service_notification_options': {
                'type': 'list',
                'ui': {
                    'title': 'Business rules service notification options',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': ['w', 'u', 'c', 'r', 'f', 's'],
                'allowed': ['w', 'u', 'c', 'r', 'f', 's', 'n']
            },
            'business_impact': {
                'type': 'integer',
                'ui': {
                    'title': 'Business impact',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': 2
            },
            'trigger': {
                'type': 'string',
                'ui': {
                    'title': 'Trigger',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': ''
            },
            'trigger_name': {
                'type': 'string',
                'ui': {
                    'title': 'Trigger name',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': ''
            },
            'trigger_broker_raise_enabled': {
                'type': 'boolean',
                'ui': {
                    'title': 'Trigger broker raise enabled',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': False
            },
            'trending_policies': {
                'type': 'list',
                'ui': {
                    'title': 'Trending policies',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': []
            },
            'checkmodulations': {
                'type': 'list',
                'ui': {
                    'title': 'Check modulations',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': []
            },
            'macromodulations': {
                'type': 'list',
                'ui': {
                    'title': 'Macro modulations',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': []
            },
            'custom_views': {
                'type': 'list',
                'ui': {
                    'title': 'Custom views',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': []
            },
            'snapshot_enabled': {
                'type': 'boolean',
                'ui': {
                    'title': 'Snapshot enabled',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': False
            },
            'snapshot_command': {
                'type': 'objectid',
                'ui': {
                    'title': 'Snapshot command',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'data_relation': {
                    'resource': 'command',
                    'embeddable': True
                },
                'nullable': True
            },
            'snapshot_period': {
                'type': 'objectid',
                'ui': {
                    'title': 'Snapshot period',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': "link"
                },
                'data_relation': {
                    'resource': 'timeperiod',
                    'embeddable': True
                },
                'nullable': True
            },
            'snapshot_criteria': {
                'type': 'list',
                'ui': {
                    'title': 'Snapshot criteria',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': ['d', 'u']
            },
            'snapshot_interval': {
                'type': 'integer',
                'ui': {
                    'title': 'Snapshot interval',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': 5
            },
            'obsess_over_host': {
                'type': 'boolean',
                'ui': {
                    'title': 'Obsess over host',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': False
            },
            '_users_read': {
                'type': 'list',
                'schema': {
                    'type': 'objectid',
                    'data_relation': {
                        'resource': 'contact',
                        'embeddable': True,
                    }
                },
            },
            '_users_update': {
                'type': 'list',
                'schema': {
                    'type': 'objectid',
                    'data_relation': {
                        'resource': 'contact',
                        'embeddable': True,
                    }
                },
            },
            '_users_delete': {
                'type': 'list',
                'schema': {
                    'type': 'objectid',
                    'data_relation': {
                        'resource': 'contact',
                        'embeddable': True,
                    }
                },
            },
            # This to define if the object in this model are to be used in the UI
            'ui': {
                'type': 'boolean',
                'default': True,
                'required': False,

                # UI parameters for the objects
                'ui': {
                    'list_title': 'Hosts list (%d items)',
                    'page_title': 'Host: %s',
                    'uid': 'host_name',
                    'visible': True,
                    'orderable': True,
                    'searchable': True
                }
            },
            '_is_template': {
                'type': 'boolean',
                'ui': {
                    'title': 'This host is a template',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': False
            },
            '_templates': {
                'type': 'list',
                'ui': {
                    'title': 'Templates to apply',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': "link"
                },
                'schema': {
                    'type': 'objectid',
                    'data_relation': {
                        'resource': 'host',
                        'embeddable': True,
                    }
                },
                'default': []
            },
            '_templates_with_services': {
                'type': 'boolean',
                'ui': {
                    'title': 'Add too services of templates hosts',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': False
            },
            '_template_fields': {
                'type': 'list',
                'ui': {
                    'title': 'Fields list use templates values',
                    'visible': True,
                    'orderable': True,
                    'searchable': True,
                    'format': None
                },
                'default': []
            },
        }
    }
