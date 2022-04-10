import logging
# import os / os.getenv("LOGLEVEL", "DEBUG").upper()

def print_vs_logging(loglevel):
    
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'

    logging.basicConfig(level=loglevel, format=fmt)

    logging.debug("debug info")
    logging.info("just some info")
    logging.error("uh oh :(")

    print("\n")

# Print ( info / errors )
print_vs_logging("INFO")

# print ( info / debug / errors )
# print_vs_logging("DEBUG")

# print ( errors )
# print_vs_logging("ERROR")
