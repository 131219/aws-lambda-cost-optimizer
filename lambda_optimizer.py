def analyze_lambda(config):
    # Validate input
    if not config or not isinstance(config, dict):
        raise ValueError('Config must be a non-empty dictionary')

    suggestions = []

    # Check timeout
    timeout = config.get('timeout')
    if timeout is None:
        raise ValueError('Missing "timeout" in config')
    elif not isinstance(timeout, (int, float)) or timeout <= 0:
        raise ValueError('"timeout" must be a positive number')
    elif timeout > 10:
        suggestions.append('Reduce timeout: Most Lambdas finish in < 10s.')

    # Check memory
    memory = config.get('memory')
    if memory is None:
        raise ValueError('Missing "memory" in config')
    elif not isinstance(memory, (int, float)) or memory <= 0:
        raise ValueError('"memory" must be a positive number')
    elif memory > 512:
        suggestions.append('Reduce memory if possible: Costs rise with allocation.')

    # Check provisioned concurrency
    provisioned = config.get('provisioned_concurrency')
    if provisioned is None:
        raise ValueError('Missing "provisioned_concurrency" in config')
    elif not isinstance(provisioned, bool):
        raise ValueError('"provisioned_concurrency" must be a boolean')
    elif not provisioned:
        suggestions.append('Enable provisioned concurrency for predictable workloads.')

    return suggestions
