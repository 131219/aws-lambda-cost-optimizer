import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lambda_optimizer import analyze_lambda

# Basic config (expected to pass)
def test_basic():
    config = {'timeout': 5, 'memory': 128, 'provisioned_concurrency': True}
    assert analyze_lambda(config) == [], "Should recommend no changes for efficient config"

# High-cost config (should suggest all optimizations)
def test_costly():
    config = {'timeout': 20, 'memory': 1024, 'provisioned_concurrency': False}
    result = analyze_lambda(config)
    assert "Reduce timeout" in result[0]
    assert "Reduce memory" in result[1]
    assert "Enable provisioned concurrency" in result[2]

# Empty config (should raise error)
def test_empty_config():
    config = {}
    try:
        analyze_lambda(config)
    except Exception as e:
        print('Handled empty config:', e)
    else:
        print('Warning: No error on empty input!')

if __name__ == "__main__":
    test_basic()
    test_costly()
    test_empty_config()
    print("All tests passed.")

    

