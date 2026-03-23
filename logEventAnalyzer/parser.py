from log_entry import LogEntry
from exceptions import LogParseException, EmptyLogException

def parse_log(line):
    try:
        if not line or not isinstance(line, str):
            raise LogParseException("Invalid log line")

        parts = line.split('|', 2)
        if len(parts) != 3 or not all(parts):
            raise LogParseException("Invalid log entry format - expected 3 components separated by '|'")
        
        timestamp, level, message = [part.strip() for part in parts]
        if not timestamp or not level or not message:
            raise LogParseException("Log entry components(timestamp, level, message) cannot be empty")

        return LogEntry(timestamp, level, message)
    except Exception as e:
        print(f"Error parsing log line: {e}")
        return None
    