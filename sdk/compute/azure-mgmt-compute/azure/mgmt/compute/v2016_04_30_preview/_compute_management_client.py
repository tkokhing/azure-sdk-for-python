# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

from . import models
from ._configuration import ComputeManagementClientConfiguration
from .operations import (
    AvailabilitySetsOperations,
    DisksOperations,
    ImagesOperations,
    SnapshotsOperations,
    UsageOperations,
    VirtualMachineExtensionImagesOperations,
    VirtualMachineExtensionsOperations,
    VirtualMachineImagesOperations,
    VirtualMachineScaleSetVMsOperations,
    VirtualMachineScaleSetsOperations,
    VirtualMachineSizesOperations,
    VirtualMachinesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential
    from azure.core.rest import HttpRequest, HttpResponse


class ComputeManagementClient(object):
    """Compute Client.

    :ivar availability_sets: AvailabilitySetsOperations operations
    :vartype availability_sets:
         azure.mgmt.compute.v2016_04_30_preview.operations.AvailabilitySetsOperations
    :ivar virtual_machine_extension_images: VirtualMachineExtensionImagesOperations operations
    :vartype virtual_machine_extension_images:
         azure.mgmt.compute.v2016_04_30_preview.operations.VirtualMachineExtensionImagesOperations
    :ivar virtual_machine_extensions: VirtualMachineExtensionsOperations operations
    :vartype virtual_machine_extensions:
         azure.mgmt.compute.v2016_04_30_preview.operations.VirtualMachineExtensionsOperations
    :ivar virtual_machines: VirtualMachinesOperations operations
    :vartype virtual_machines:
         azure.mgmt.compute.v2016_04_30_preview.operations.VirtualMachinesOperations
    :ivar virtual_machine_images: VirtualMachineImagesOperations operations
    :vartype virtual_machine_images:
         azure.mgmt.compute.v2016_04_30_preview.operations.VirtualMachineImagesOperations
    :ivar usage: UsageOperations operations
    :vartype usage: azure.mgmt.compute.v2016_04_30_preview.operations.UsageOperations
    :ivar virtual_machine_sizes: VirtualMachineSizesOperations operations
    :vartype virtual_machine_sizes:
         azure.mgmt.compute.v2016_04_30_preview.operations.VirtualMachineSizesOperations
    :ivar images: ImagesOperations operations
    :vartype images: azure.mgmt.compute.v2016_04_30_preview.operations.ImagesOperations
    :ivar virtual_machine_scale_sets: VirtualMachineScaleSetsOperations operations
    :vartype virtual_machine_scale_sets:
         azure.mgmt.compute.v2016_04_30_preview.operations.VirtualMachineScaleSetsOperations
    :ivar virtual_machine_scale_set_vms: VirtualMachineScaleSetVMsOperations operations
    :vartype virtual_machine_scale_set_vms:
         azure.mgmt.compute.v2016_04_30_preview.operations.VirtualMachineScaleSetVMsOperations
    :ivar disks: DisksOperations operations
    :vartype disks: azure.mgmt.compute.v2016_04_30_preview.operations.DisksOperations
    :ivar snapshots: SnapshotsOperations operations
    :vartype snapshots: azure.mgmt.compute.v2016_04_30_preview.operations.SnapshotsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure
         subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param base_url: Service URL
    :type base_url: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = "https://management.azure.com"
        self._config = ComputeManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.availability_sets = AvailabilitySetsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_machine_extension_images = VirtualMachineExtensionImagesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_machine_extensions = VirtualMachineExtensionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_machines = VirtualMachinesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_machine_images = VirtualMachineImagesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.usage = UsageOperations(self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_sizes = VirtualMachineSizesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.images = ImagesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_scale_sets = VirtualMachineScaleSetsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_machine_scale_set_vms = VirtualMachineScaleSetVMsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.disks = DisksOperations(self._client, self._config, self._serialize, self._deserialize)
        self.snapshots = SnapshotsOperations(self._client, self._config, self._serialize, self._deserialize)

    def _send_request(
        self,
        request,  # type: HttpRequest
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpResponse
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `azure.mgmt.compute.v2016_04_30_preview.rest`.
        Use these helper methods to create the request you pass to this method. See our example below:


        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        For advanced cases, you can also create your own :class:`~azure.core.rest.HttpRequest`
        and pass it in.

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> ComputeManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
