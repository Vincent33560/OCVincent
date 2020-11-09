import time
import progressbar
progressbar1 = progressbar
for i in progressbar(range(100), redirect_stdout=True):
    print('Some text', i)
    time.sleep(0.1)