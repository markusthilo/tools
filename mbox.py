#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import email
from email.policy import default


class MboxReader:
    def __init__(self, filename):
        self.handle = open(filename, 'rb')
        assert self.handle.readline().startswith(b'From ')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.handle.close()

    def __iter__(self):
        return iter(self.__next__())

    def __next__(self):
        lines = []
        while True:
            line = self.handle.readline()
            if line == b'' or line.startswith(b'From '):
                yield email.message_from_bytes(b''.join(lines), policy=default)
                if line == b'':
                    break
                lines = []
                continue
            if line.startswith(b'>') and line.lstrip(b'>').startswith(b'From '):
                line = line[1:]
            lines.append(line)

#with open('Output.txt','w',encoding="utf-8") as file:
#    for idx,message in tqdm(enumerate(mbox)):
#        # print(message.keys())
#        mail_from = f"{str(message['From'])}\n".replace('"','')
#        file.write(mail_from)
#        print(idx,message['From'])
