import sys
import os
sys.path.extend([sub_directory[0] for sub_directory in os.walk(os.path.dirname(__file__))])

import server.server as server

if __name__ == '__main__':
    server.run()
