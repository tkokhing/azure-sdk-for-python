# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ...operations._virtual_machine_scale_set_rolling_upgrades_operations import (
    build_cancel_request_initial,
    build_get_latest_request,
    build_start_extension_upgrade_request_initial,
    build_start_os_upgrade_request_initial,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class VirtualMachineScaleSetRollingUpgradesOperations:
    """VirtualMachineScaleSetRollingUpgradesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.compute.v2021_03_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def _cancel_initial(self, resource_group_name: str, vm_scale_set_name: str, **kwargs: Any) -> None:
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_cancel_request_initial(
            resource_group_name=resource_group_name,
            vm_scale_set_name=vm_scale_set_name,
            subscription_id=self._config.subscription_id,
            template_url=self._cancel_initial.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _cancel_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/rollingUpgrades/cancel"}  # type: ignore

    async def begin_cancel(
        self, resource_group_name: str, vm_scale_set_name: str, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Cancels the current virtual machine scale set rolling upgrade.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set.
        :type vm_scale_set_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._cancel_initial(
                resource_group_name=resource_group_name,
                vm_scale_set_name=vm_scale_set_name,
                cls=lambda x, y, z: x,
                **kwargs
            )

        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method = AsyncARMPolling(lro_delay, **kwargs)
        elif polling is False:
            polling_method = AsyncNoPolling()
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        else:
            return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_cancel.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/rollingUpgrades/cancel"}  # type: ignore

    async def _start_os_upgrade_initial(self, resource_group_name: str, vm_scale_set_name: str, **kwargs: Any) -> None:
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_start_os_upgrade_request_initial(
            resource_group_name=resource_group_name,
            vm_scale_set_name=vm_scale_set_name,
            subscription_id=self._config.subscription_id,
            template_url=self._start_os_upgrade_initial.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _start_os_upgrade_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/osRollingUpgrade"}  # type: ignore

    async def begin_start_os_upgrade(
        self, resource_group_name: str, vm_scale_set_name: str, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Starts a rolling upgrade to move all virtual machine scale set instances to the latest
        available Platform Image OS version. Instances which are already running the latest available
        OS version are not affected.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set.
        :type vm_scale_set_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._start_os_upgrade_initial(
                resource_group_name=resource_group_name,
                vm_scale_set_name=vm_scale_set_name,
                cls=lambda x, y, z: x,
                **kwargs
            )

        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method = AsyncARMPolling(lro_delay, **kwargs)
        elif polling is False:
            polling_method = AsyncNoPolling()
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        else:
            return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_start_os_upgrade.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/osRollingUpgrade"}  # type: ignore

    async def _start_extension_upgrade_initial(
        self, resource_group_name: str, vm_scale_set_name: str, **kwargs: Any
    ) -> None:
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_start_extension_upgrade_request_initial(
            resource_group_name=resource_group_name,
            vm_scale_set_name=vm_scale_set_name,
            subscription_id=self._config.subscription_id,
            template_url=self._start_extension_upgrade_initial.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _start_extension_upgrade_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensionRollingUpgrade"}  # type: ignore

    async def begin_start_extension_upgrade(
        self, resource_group_name: str, vm_scale_set_name: str, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Starts a rolling upgrade to move all extensions for all virtual machine scale set instances to
        the latest available extension version. Instances which are already running the latest
        extension versions are not affected.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set.
        :type vm_scale_set_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._start_extension_upgrade_initial(
                resource_group_name=resource_group_name,
                vm_scale_set_name=vm_scale_set_name,
                cls=lambda x, y, z: x,
                **kwargs
            )

        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method = AsyncARMPolling(lro_delay, **kwargs)
        elif polling is False:
            polling_method = AsyncNoPolling()
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        else:
            return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_start_extension_upgrade.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensionRollingUpgrade"}  # type: ignore

    async def get_latest(
        self, resource_group_name: str, vm_scale_set_name: str, **kwargs: Any
    ) -> "_models.RollingUpgradeStatusInfo":
        """Gets the status of the latest virtual machine scale set rolling upgrade.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set.
        :type vm_scale_set_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RollingUpgradeStatusInfo, or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2021_03_01.models.RollingUpgradeStatusInfo
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.RollingUpgradeStatusInfo"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_latest_request(
            resource_group_name=resource_group_name,
            vm_scale_set_name=vm_scale_set_name,
            subscription_id=self._config.subscription_id,
            template_url=self.get_latest.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("RollingUpgradeStatusInfo", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_latest.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/rollingUpgrades/latest"}  # type: ignore
