"""AWS Lambda Cost Optimizer"""

def analyze_lambda(config):
    """Analyzes Lambda config for cost optimization."""
    suggestions = []
    if config.get('timeout', 3) > 15:
        suggestions.append("Reduce timeout: Most Lambdas finish in < 10s.")
    if config.get('memory', 128) > 512:
        suggestions.append("Reduce memory if possible: Costs rise with allocation.")
    if not config.get('provisioned_concurrency'):
        suggestions.append("Enable provisioned concurrency for predictable workloads.")
    return suggestions

# Example usage
if __name__ == "__main__":
    lambda_config = {
        'timeout': 20,
        'memory': 1024,
        'provisioned_concurrency': False
    }
    print(analyze_lambda(lambda_config))
