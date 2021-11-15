import os

REGION = os.environ.get('REGION')
PROJECT_ID = os.environ.get('PROJECT_ID')
REGISTRY_ID = os.environ.get('REGISTRY_ID')

CERTIFICATE_FILE_PATH = "./keys/roots.pem"
PRIVATE_KEY_FILE_PATH = "./keys/rsa_private.pem"

DEFAULT_TOPIC = "events"
TELEMETRY_TOPIC = "events/telemetry"

