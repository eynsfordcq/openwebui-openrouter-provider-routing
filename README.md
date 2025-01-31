# Openrouter Provider Routing

This function allows you to configure how OpenRouter selects providers for handling requests. You can set a prioritized list of providers and control whether to allow fallbacks to other providers if none in the list are available. See [openrouter docs](https://openrouter.ai/docs/provider-routing#custom-routing).

## Setup

1. Import the function.
2. Enable the function.
3. Configure valve:
    - **Providers**: A list of providers separated by comma. E.g. `DeepSeek,Nebius,DeepInfra`
    - **Allow Fallbacks**: Toggle on/off to enable fallbacks to providers not listed in the previous list.
4. Enable the function for Openrouter's model.
    - Navigate to "Models" in Admin tab.
    - Select the model you want to enable this function.
    - Under "filters", check the Openrouter Provider Routing function.