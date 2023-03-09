from obspy import UTCDateTime
from obspy.clients.seedlink import Client

# Open a file for writing
with open("data.txt", "w") as f:
    client = Client("geofon.gfz-potsdam.de", 18000)
    buffer_size = 60  # in seconds
    endtime = UTCDateTime.now()
    starttime = endtime - buffer_size

    # Continuously get the waveform data and save to file
    while True:
        st = client.get_waveforms("RO", "VRI", "", "EHZ", starttime, endtime)
        trace = st[0]
        data = trace.data
        
        # Write the waveform data to the file
        for value in data:
            f.write(str(value) + "\n")
        
        print("Minimum value: ", min(data), "Maximum value: ", max(data))

        # Update the start and end times for the next iteration
        endtime = UTCDateTime.now()
        starttime = endtime - buffer_size
