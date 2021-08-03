# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ...operations._dedicated_host_groups_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_request,
    build_list_by_resource_group_request,
    build_list_by_subscription_request,
    build_update_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class DedicatedHostGroupsOperations:
    """DedicatedHostGroupsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.compute.v2019_12_01.models
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

    async def create_or_update(
        self, resource_group_name: str, host_group_name: str, parameters: "_models.DedicatedHostGroup", **kwargs: Any
    ) -> "_models.DedicatedHostGroup":
        """Create or update a dedicated host group. For details of Dedicated Host and Dedicated Host
        Groups please see [Dedicated Host Documentation]
        (https://go.microsoft.com/fwlink/?linkid=2082596).

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param host_group_name: The name of the dedicated host group.
        :type host_group_name: str
        :param parameters: Parameters supplied to the Create Dedicated Host Group.
        :type parameters: ~azure.mgmt.compute.v2019_12_01.models.DedicatedHostGroup
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DedicatedHostGroup, or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2019_12_01.models.DedicatedHostGroup
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.DedicatedHostGroup"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(parameters, "DedicatedHostGroup")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            host_group_name=host_group_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=json,
            template_url=self.create_or_update.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("DedicatedHostGroup", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("DedicatedHostGroup", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}"}  # type: ignore

    async def update(
        self,
        resource_group_name: str,
        host_group_name: str,
        parameters: "_models.DedicatedHostGroupUpdate",
        **kwargs: Any
    ) -> "_models.DedicatedHostGroup":
        """Update an dedicated host group.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param host_group_name: The name of the dedicated host group.
        :type host_group_name: str
        :param parameters: Parameters supplied to the Update Dedicated Host Group operation.
        :type parameters: ~azure.mgmt.compute.v2019_12_01.models.DedicatedHostGroupUpdate
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DedicatedHostGroup, or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2019_12_01.models.DedicatedHostGroup
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.DedicatedHostGroup"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(parameters, "DedicatedHostGroupUpdate")

        request = build_update_request(
            resource_group_name=resource_group_name,
            host_group_name=host_group_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=json,
            template_url=self.update.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("DedicatedHostGroup", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}"}  # type: ignore

    async def delete(self, resource_group_name: str, host_group_name: str, **kwargs: Any) -> None:
        """Delete a dedicated host group.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param host_group_name: The name of the dedicated host group.
        :type host_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_delete_request(
            resource_group_name=resource_group_name,
            host_group_name=host_group_name,
            subscription_id=self._config.subscription_id,
            template_url=self.delete.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}"}  # type: ignore

    async def get(self, resource_group_name: str, host_group_name: str, **kwargs: Any) -> "_models.DedicatedHostGroup":
        """Retrieves information about a dedicated host group.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param host_group_name: The name of the dedicated host group.
        :type host_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DedicatedHostGroup, or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2019_12_01.models.DedicatedHostGroup
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.DedicatedHostGroup"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_request(
            resource_group_name=resource_group_name,
            host_group_name=host_group_name,
            subscription_id=self._config.subscription_id,
            template_url=self.get.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("DedicatedHostGroup", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}"}  # type: ignore

    def list_by_resource_group(
        self, resource_group_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.DedicatedHostGroupListResult"]:
        """Lists all of the dedicated host groups in the specified resource group. Use the nextLink
        property in the response to get the next page of dedicated host groups.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either DedicatedHostGroupListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.compute.v2019_12_01.models.DedicatedHostGroupListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.DedicatedHostGroupListResult"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_resource_group_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    template_url=self.list_by_resource_group.metadata["url"],
                )._to_pipeline_transport_request()
                request.url = self._client.format_url(request.url)

            else:

                request = build_list_by_resource_group_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )._to_pipeline_transport_request()
                request.url = self._client.format_url(request.url)

                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("DedicatedHostGroupListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_by_resource_group.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups"}  # type: ignore

    def list_by_subscription(self, **kwargs: Any) -> AsyncIterable["_models.DedicatedHostGroupListResult"]:
        """Lists all of the dedicated host groups in the subscription. Use the nextLink property in the
        response to get the next page of dedicated host groups.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either DedicatedHostGroupListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.compute.v2019_12_01.models.DedicatedHostGroupListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.DedicatedHostGroupListResult"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_subscription_request(
                    subscription_id=self._config.subscription_id,
                    template_url=self.list_by_subscription.metadata["url"],
                )._to_pipeline_transport_request()
                request.url = self._client.format_url(request.url)

            else:

                request = build_list_by_subscription_request(
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )._to_pipeline_transport_request()
                request.url = self._client.format_url(request.url)

                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("DedicatedHostGroupListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_by_subscription.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/hostGroups"}  # type: ignore
