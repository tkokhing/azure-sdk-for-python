# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar
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
from azure.core.rest import HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ...operations._virtual_machine_images_operations import (
    build_get_request,
    build_list_offers_request,
    build_list_publishers_request,
    build_list_request,
    build_list_skus_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class VirtualMachineImagesOperations:
    """VirtualMachineImagesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.compute.v2016_03_30.models
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

    async def get(
        self, location: str, publisher_name: str, offer: str, skus: str, version: str, **kwargs: Any
    ) -> "_models.VirtualMachineImage":
        """Gets a virtual machine image.

        :param location: The name of a supported Azure region.
        :type location: str
        :param publisher_name: A valid image publisher.
        :type publisher_name: str
        :param offer: A valid image publisher offer.
        :type offer: str
        :param skus: A valid image SKU.
        :type skus: str
        :param version: A valid image SKU version.
        :type version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: VirtualMachineImage, or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2016_03_30.models.VirtualMachineImage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.VirtualMachineImage"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_request(
            location=location,
            publisher_name=publisher_name,
            offer=offer,
            skus=skus,
            version=version,
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

        deserialized = self._deserialize("VirtualMachineImage", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus/{skus}/versions/{version}"}  # type: ignore

    async def list(
        self,
        location: str,
        publisher_name: str,
        offer: str,
        skus: str,
        expand: Optional[str] = None,
        top: Optional[int] = None,
        orderby: Optional[str] = None,
        **kwargs: Any
    ) -> List["_models.VirtualMachineImageResource"]:
        """Gets a list of all virtual machine image versions for the specified location, publisher, offer,
        and SKU.

        :param location: The name of a supported Azure region.
        :type location: str
        :param publisher_name: A valid image publisher.
        :type publisher_name: str
        :param offer: A valid image publisher offer.
        :type offer: str
        :param skus: A valid image SKU.
        :type skus: str
        :param expand: The expand expression to apply on the operation.
        :type expand: str
        :param top:
        :type top: int
        :param orderby:
        :type orderby: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of VirtualMachineImageResource, or the result of cls(response)
        :rtype: list[~azure.mgmt.compute.v2016_03_30.models.VirtualMachineImageResource]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[List["_models.VirtualMachineImageResource"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_list_request(
            location=location,
            publisher_name=publisher_name,
            offer=offer,
            skus=skus,
            subscription_id=self._config.subscription_id,
            expand=expand,
            top=top,
            orderby=orderby,
            template_url=self.list.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("[VirtualMachineImageResource]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus/{skus}/versions"}  # type: ignore

    async def list_offers(
        self, location: str, publisher_name: str, **kwargs: Any
    ) -> List["_models.VirtualMachineImageResource"]:
        """Gets a list of virtual machine image offers for the specified location and publisher.

        :param location: The name of a supported Azure region.
        :type location: str
        :param publisher_name: A valid image publisher.
        :type publisher_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of VirtualMachineImageResource, or the result of cls(response)
        :rtype: list[~azure.mgmt.compute.v2016_03_30.models.VirtualMachineImageResource]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[List["_models.VirtualMachineImageResource"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_list_offers_request(
            location=location,
            publisher_name=publisher_name,
            subscription_id=self._config.subscription_id,
            template_url=self.list_offers.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("[VirtualMachineImageResource]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_offers.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers"}  # type: ignore

    async def list_publishers(self, location: str, **kwargs: Any) -> List["_models.VirtualMachineImageResource"]:
        """Gets a list of virtual machine image publishers for the specified Azure location.

        :param location: The name of a supported Azure region.
        :type location: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of VirtualMachineImageResource, or the result of cls(response)
        :rtype: list[~azure.mgmt.compute.v2016_03_30.models.VirtualMachineImageResource]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[List["_models.VirtualMachineImageResource"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_list_publishers_request(
            location=location,
            subscription_id=self._config.subscription_id,
            template_url=self.list_publishers.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("[VirtualMachineImageResource]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_publishers.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers"}  # type: ignore

    async def list_skus(
        self, location: str, publisher_name: str, offer: str, **kwargs: Any
    ) -> List["_models.VirtualMachineImageResource"]:
        """Gets a list of virtual machine image SKUs for the specified location, publisher, and offer.

        :param location: The name of a supported Azure region.
        :type location: str
        :param publisher_name: A valid image publisher.
        :type publisher_name: str
        :param offer: A valid image publisher offer.
        :type offer: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of VirtualMachineImageResource, or the result of cls(response)
        :rtype: list[~azure.mgmt.compute.v2016_03_30.models.VirtualMachineImageResource]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[List["_models.VirtualMachineImageResource"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_list_skus_request(
            location=location,
            publisher_name=publisher_name,
            offer=offer,
            subscription_id=self._config.subscription_id,
            template_url=self.list_skus.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("[VirtualMachineImageResource]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_skus.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus"}  # type: ignore
