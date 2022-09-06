#!/usr/bin/env python3

import sys
import socket
import selectors
import traceback
import loger
from codigo import libclient,executionrow



def run_client(action):
    sel = selectors.DefaultSelector()
    #create the request -> actions
    def create_request(action):
        loger.logger.info("creating the request")
        if action == "config":
            return dict(
                type="text/json",
                encoding="utf-8",
                #msg 
                content=dict(action=action),
            )
        elif action == "search":
            return dict(
                type="text/json",
                encoding="utf-8",
                content=dict(action=action, pc=executionrow.send_information()),
            )
        else:
            return dict(
                type="binary/custom-client-binary-type",
                encoding="binary",
                content=bytes(action, encoding="utf-8"),
            )


    def start_connection(host, port, request):
        addr = (host, port)
        print(f"Starting connection to {addr}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        message = libclient.Message(sel, sock, addr, request)
        sel.register(sock, events, data=message)

    host, port = "127.55.99.1", 65432
    #action, value = "search", "ring"
    request = create_request(action)
    start_connection(host, port, request)

    try:
        while True:
            events = sel.select(timeout=1)
            for key, mask in events:
                message = key.data
                try:
                    message.process_events(mask)
                except Exception:
                    print(
                        f"Main: Error: Exception for {message.addr}:\n"
                        f"{traceback.format_exc()}"
                    )
                    message.close()
            # Check for a socket being monitored to continue.
            if not sel.get_map():
                break
    except KeyboardInterrupt:
        print("Caught keyboard interrupt, exiting")
    finally:
        sel.close()
