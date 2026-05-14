import logging


logging.basicConfig( filename= "app.log",level=logging.DEBUG, filemode="a"
                    , format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug('Water Temp check')
logging.info('Brewing Started')
logging.warning('Water level is low')
logging.error('No water found')
logging.critical('machine shutting down')


print("Logging data written successfully")


# By default the log level is warning
# Means when you run code you can't see and debug messaged
# Debug <info <warning < error < critical 
# Default format : loglevel : username : message 
# a is append mode means add new logs at the end of the file 
# w mode will delte the old data and add latest logs only 




