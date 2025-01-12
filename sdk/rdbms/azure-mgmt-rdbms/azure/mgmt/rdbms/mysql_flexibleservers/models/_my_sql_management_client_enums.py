# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class ConfigurationSource(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Source of the configuration.
    """

    SYSTEM_DEFAULT = "system-default"
    USER_OVERRIDE = "user-override"

class CreatedByType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class CreateMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The mode to create a new MySQL server.
    """

    DEFAULT = "Default"
    POINT_IN_TIME_RESTORE = "PointInTimeRestore"
    REPLICA = "Replica"
    GEO_RESTORE = "GeoRestore"

class EnableStatusEnum(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to indicate whether value is 'Enabled' or 'Disabled'
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class HighAvailabilityMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """High availability mode for a server.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"
    ZONE_REDUNDANT = "ZoneRedundant"
    SAME_ZONE = "SameZone"

class HighAvailabilityState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The state of server high availability.
    """

    NOT_ENABLED = "NotEnabled"
    CREATING_STANDBY = "CreatingStandby"
    HEALTHY = "Healthy"
    FAILING_OVER = "FailingOver"
    REMOVING_STANDBY = "RemovingStandby"

class IsConfigPendingRestart(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """If is the configuration pending restart or not.
    """

    TRUE = "True"
    FALSE = "False"

class IsDynamicConfig(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """If is the configuration dynamic.
    """

    TRUE = "True"
    FALSE = "False"

class IsReadOnly(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """If is the configuration read only.
    """

    TRUE = "True"
    FALSE = "False"

class ReplicationRole(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The replication role.
    """

    NONE = "None"
    SOURCE = "Source"
    REPLICA = "Replica"

class ServerState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The state of a server.
    """

    READY = "Ready"
    DROPPING = "Dropping"
    DISABLED = "Disabled"
    STARTING = "Starting"
    STOPPING = "Stopping"
    STOPPED = "Stopped"
    UPDATING = "Updating"

class ServerVersion(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The version of a server.
    """

    FIVE7 = "5.7"
    EIGHT0_21 = "8.0.21"

class SkuTier(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The tier of the particular SKU, e.g. GeneralPurpose.
    """

    BURSTABLE = "Burstable"
    GENERAL_PURPOSE = "GeneralPurpose"
    MEMORY_OPTIMIZED = "MemoryOptimized"
