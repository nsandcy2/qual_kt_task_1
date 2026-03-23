from log_entry import LogEntry
from analyzer import LogAnalyzer
analyzer = LogAnalyzer()
analyzer.add_log("2024-06-01 12:00:00| INFO | User logged in")
analyzer.add_log("2024-06-01 12:01:00| ERROR | Database connection failed")
analyzer.add_log("2024-06-01 12:01:50| ERROR | Database connection failed")
analyzer.add_log("2024-06-01 12:01:55| ERROR | Database connection failed")
analyzer.add_log("2024-06-01 12:02:00| INFO | User logged out")
analyzer.add_log("2024-06-01 12:00:00| INFO | User logged in")
# analyzer.add_log("") #empty log entry
# analyzer.add_log("2024-06-01 12:00:00| INFO ") #invalid format log entry
# analyzer.add_log(678) #invalid type log entry
# analyzer.add_log() #missing argument log entry
print("level summary:", analyzer.get_level_summary())

print( "top messages:", analyzer.get_top_messages(1))  