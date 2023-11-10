import ftplib
import threading
from queue import Queue
from googlesearch import search

class FTPWorkerThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Get the FTP site from the queue
            ftp_site = self.queue.get()

            # Perform FTP operations
            self.process_ftp_site(ftp_site)

            # Signal that the task is complete
            self.queue.task_done()

    def process_ftp_site(self, ftp_site):
        try:
            print(f"Connecting to {ftp_site}")
            with ftplib.FTP(ftp_site) as ftp:
                ftp.login()  # You may need to provide credentials here

                # List the root directory or retrieve first N files
                # Modify this part based on your specific requirements
                ftp.retrlines('LIST')
        except Exception as e:
            print(f"Error accessing {ftp_site}: {e}")

def search_ftp_sites(query, num_results=10):
    ftp_sites = list(search(query, num_results=num_results))

    return ftp_sites

def main():
    # Use Google search to find FTP sites with the specified criteria
    search_query = 'inurl:ftp -inurl:(http|https)'
    ftp_sites = search_ftp_sites(search_query, num_results=20)

    # Create a queue to hold the FTP sites
    queue = Queue()

    # Create and start worker threads
    for _ in range(5):  # You can adjust the number of threads
        worker = FTPWorkerThread(queue)
        worker.daemon = True
        worker.start()

    # Enqueue FTP sites
    for ftp_site in ftp_sites:
        queue.put(ftp_site)

    # Wait for all tasks to be completed
    queue.join()

if __name__ == "__main__":
    main()
 