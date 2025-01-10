import logging

import numpy

from ezndi.api import initialize_ndi, destroy_ndi, create_ndi_sender, destroy_ndi_sender, send_frame


if __name__ == "__main__":
    initialize_ndi()

    name_sender = "ezndi"
    sender = create_ndi_sender(name_sender)

    print(f"start broadcasting {name_sender}")
    while True: # loop to broadcast random image
        try:
            image = numpy.random.rand(720, 1280, 3)
            send_frame(sender, image, fps=60)
        except KeyboardInterrupt: # if you want to stop broadcasting, press Ctrl+C
            print("stop broadcasting")
            break
        except Exception as e: # logging exception
            logging.warning(f"{e}")

    destroy_ndi_sender(sender)
    destroy_ndi()
