# Openrouter Provider Routing

This function allows you to configure how OpenRouter selects providers for handling requests. You can set a prioritized list of providers and control whether to allow fallbacks to other providers if none in the list are available. See [openrouter docs](https://openrouter.ai/docs/provider-routing#custom-routing).

## Setup

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