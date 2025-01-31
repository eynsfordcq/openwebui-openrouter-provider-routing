"""
title: Openrouter Provider Routing
author: eynsfordcq
github_url: https://github.com/eynsfordcq/openwebui-openrouter-provider-routing
openrouter_reference: https://openrouter.ai/docs/provider-routing#custom-routing
version: 0.1
"""

from pydantic import BaseModel, Field
from typing import List

class Filter:
    class Valves(BaseModel):
        providers: List[str] = Field(
            default=None, 
            description="A prioritized list of providers that OpenRouter \
                will attempt to use in the specified order. \
                If left empty, OpenRouter will automatically balance \
                requests across top providers"
        )
        allow_fallbacks: bool = Field(
            default=False,
            description="If enabled, OpenRouter will try providers \
                outside the specified list if none are operational. \
                Disabling this ensures requests fail instead of switching \
                to other providers."
        )

    def __init__(self):
        self.valves = self.Valves()

    def inlet(self, body: dict) -> dict:
        if self.valves.providers:
            body["provider"] = {
                "order": self.valves.providers,
                "allow_fallbacks": self.valves.allow_fallbacks,
            }

            print(
                f"openrouter_provider_routing(): "
                f"using providers: {body['provider']['order']}"
            )
            print(
                f"openrouter_provider_routing(): "
                f"allow fallback: {body['provider']['allow_fallbacks']}"
            )
        
        return body