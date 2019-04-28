import numpy as np
import pandas as pd
from datetime import datetime

# result from Google Calendar API FreeBusy call
free_busy = {
 "kind": "calendar#freeBusy",
 "timeMin": "2019-04-18T20:46:00.000Z",
 "timeMax": "2019-04-30T20:46:00.000Z",
 "calendars": {
  "yoolen@gmail.com": {
   "busy": [
    {
     "start": "2019-04-29T04:00:00Z",
     "end": "2019-04-30T20:46:00Z"
    }
   ]
  }
 }
}

today = datetime.now().date()
times = pd.period_range(today, periods=48, freq='30T')
df = pd.DataFrame(columns=['user']+list(times))
print(df)
