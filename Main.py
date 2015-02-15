# This file is part of ErasGamesBot.
# 
# ErasGamesBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
# 
# ErasGamesBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with ErasGamesBot. If not, see <http://www.gnu.org/licenses/>.
import socket
import time
import random

nicknumb = random.randint(0,999)

bot_owner = "Meandonlymeandnooneelse"
nick = "pietsbot" + str(nicknumb)
chan = "#erasgames"
sock = socket.socket()
sock.connect(("irc.freenode.net",6667))
sock.send("USER " + nick + " 0 * :" + bot_owner + "\r\n")
sock.send("NICK " + nick + "\r\n")

def msg(msg):
    return sock.send("PRIVMSG " + chan + " :" + msg + "\r\n")

def notice(msg, nick):
    return sock.send("NOTICE " + nick + " :" + msg + "\r\n")

def getsender(data):
    senderTemp = data.split("!")[0]
    sender = senderTemp.split(":")[1]
    print "Sender: " + sender
    return sender

while 1:
    data = sock.recv(512)
    print data
    if data[0:4] == "PING":
        sock.send(data.replace("PING", "PONG"))
    if data[0]!=':':
        continue
    if data.split(" ")[1] == "001":
        sock.send("MODE " + nick + " +B\r\n")
        sock.send("JOIN " + chan + "\r\n")
    elif data.split(" ")[1] == "PRIVMSG":
        msg("sorry, Ill shut up.")
