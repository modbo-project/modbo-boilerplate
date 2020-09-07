import time

def wait_for_job_unschedule(job):
    while job.next_t:
        time.sleep(0.1)
