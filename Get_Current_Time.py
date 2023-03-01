import boto3
from datetime import datetime
import pytz

# Get the timezone object for Eastern Timezone
tz_ET = pytz.timezone('America/New_York')

# Get the current time in New York
datetime_ET = datetime.now(tz_ET)

# Format the time as a string and print it
print("US Eastern current time:", datetime_ET.strftime("%I:%M:%S %p"))