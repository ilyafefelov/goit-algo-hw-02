import queue
import random
import time


class ServiceCenter:
    """
    Represents a service center that generates and processes requests.

    Attributes:
        request_queue (Queue): A queue to store the generated requests.

    Methods:
        generate_request: Generates a request with a random ID and adds it to the request queue.
        process_request: Processes the next request in the request queue, if any.
    """

    def __init__(self):
        self.request_queue = queue.Queue()

    def generate_request(self):
        """
        Generates a request with a random ID and adds it to the request queue.
        """
        request_id = random.randint(1000, 9999)
        print(f"Generating request with ID: {request_id}")
        self.request_queue.put(request_id)

    def process_request(self):
        """
        Processes the next request in the request queue, if any.
        """
        if not self.request_queue.empty():
            request_id = self.request_queue.get()
            print(f"Processing request with ID: {request_id}")
        else:
            print("-----------------------------------")
            print("No requests to process!!!")


def main():
    service_center = ServiceCenter()

    while True:
        print(
            "\nService Center Menu:",
            "Queue Size:",
            service_center.request_queue.qsize(),
            "Queue Contents:",
            list(service_center.request_queue.queue),
            sep="\n",
        )
        action = (
            input(
                "Enter 'g' to generate a request, 'p' to process a request, 'q' to quit: "
            )
            .strip()
            .lower()
        )
        if action == "g":
            service_center.generate_request()
        elif action == "p":
            service_center.process_request()
        elif action == "q":
            break
        else:
            print("Invalid input. Please enter 'g', 'p', or 'q'.")


if __name__ == "__main__":
    main()
