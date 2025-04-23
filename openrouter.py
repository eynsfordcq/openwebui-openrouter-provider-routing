"""
title: Openrouter Provider Routing
author: eynsfordcq
github_url: https://github.com/eynsfordcq/openwebui-openrouter-provider-routing
openrouter_reference: https://openrouter.ai/docs/features/provider-routing
version: 0.2

How to use:
1. Import the function.
2. Enable the function.
3. Configure valve:
    - Configure the valve accordingly, refer openrouter reference for more info.
4. Enable the function for Openrouter's model.
    - Navigate to "Models" in Admin tab.
    - Select the model you want to enable this function.
    - Under "filters", check the Openrouter Provider Routing function.
5. Alternatively, create a model under "workspace"
    - Navigate to "workspace".
    - Click the "+" button in "models" tab.
    - Enter model name, model id, and select desired a base model.
    - Under "filters", check the this function.
6. Check logs for the configuration sent in body and https://openrouter.ai/activity for verification.
"""

import logging
from typing import List, Literal, Optional

from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

class Filter:
    class Valves(BaseModel):
        order: List[str] = Field(
            default=None,
            description="A prioritized list of provider names to try in order. \
                (e.g. [\"Anthropic\", \"OpenAI\"])",
        )
        allow_fallbacks: bool = Field(
            default=True, 
            description="Whether to allow backup providers when the primary \
                is unavailable. Defaults to true.",
        )
        require_parameters: bool = Field(
            default=False,
            description="Only use providers that support all parameters in \
                the request. Defaults to false.",
        )
        data_collection: Literal["allow", "deny"] = Field(
            default="allow", 
            description="Control whether to use providers that may store data. \
                Defaults to \"allow\".",
        )
        ignore: Optional[List[str]] = Field(
            default=None,
            description="List of provider names to skip for this request.",
        )
        quantizations: Optional[List[str]] = Field(
            default=None,
            description="List of quantization levels to filter by \
                (e.g., ['int4', 'int8']).",
        )
        sort: Optional[Literal["price", "throughput", "latency"]] = Field(
            default=None,
            description="Sort providers by price, throughput, or latency.",
        )

    def __init__(self):
        self.valves = self.Valves()

    def inlet(self, body: dict) -> dict:
        config = self.valves.model_dump(
            exclude_none=True,
            exclude_defaults=True
        )

        if config:
            body["provider"] = config
            logger.info(f"using provider config: {config}")
        
        return body