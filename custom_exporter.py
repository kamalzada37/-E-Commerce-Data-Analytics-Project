from prometheus_client import start_http_server, Gauge, Counter, Histogram
import random, time

# Define metrics
TEMPERATURE = Gauge('weather_temperature_celsius', 'Current temperature in Celsius')
API_RESPONSE_TIME = Histogram('api_response_time_seconds', 'Response time of fake API')
API_REQUEST_COUNT = Counter('api_request_total', 'Total number of API requests made')

def collect_metrics():
    """Simulate external API data collection"""
    while True:
        # Fake temperature between 10 and 35°C
        temp = random.uniform(10.0, 35.0)
        TEMPERATURE.set(temp)

        # Fake response time between 0.1 and 1.5 seconds
        response_time = random.uniform(0.1, 1.5)
        API_RESPONSE_TIME.observe(response_time)

        # Increment request count
        API_REQUEST_COUNT.inc()

        print(f"Collected metrics → Temp: {temp:.2f}°C | Response time: {response_time:.2f}s")

        time.sleep(5)

if __name__ == "__main__":
    print("🚀 Starting custom Prometheus exporter on port 8000...")
    start_http_server(8000)
    collect_metrics()
