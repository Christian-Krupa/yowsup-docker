# -*- coding: utf-8 -*-

# inspired by mintos002 - https://github.com/tgalal/yowsup/issues/1658

import sys,os, subprocess, time

from yowsup.layers.interface                           import YowInterfaceLayer					#Reply to the message
from yowsup.layers.interface                           import ProtocolEntityCallback			#Reply to the message
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity			#Body message
from yowsup.layers.protocol_presence.protocolentities  import AvailablePresenceProtocolEntity   #Online
from yowsup.layers.protocol_presence.protocolentities  import UnavailablePresenceProtocolEntity #Offline
from yowsup.layers.protocol_presence.protocolentities  import PresenceProtocolEntity			#Name presence
from yowsup.layers.protocol_chatstate.protocolentities import OutgoingChatstateProtocolEntity	#is writing, writing pause
from yowsup.common.tools                               import Jid 								#is writing, writing pause

class EchoLayer(YowInterfaceLayer):
    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        if messageProtocolEntity.getType() == 'text':
            #print "text"
            self.toLower(messageProtocolEntity.ack()) #Set received (double v)
            time.sleep(0.5)
            #self.toLower(PresenceProtocolEntity(name = name)) #Set name Presence
            #time.sleep(0.5)
            self.toLower(AvailablePresenceProtocolEntity()) #Set online
            time.sleep(0.5)
            self.toLower(messageProtocolEntity.ack(True)) #Set read (double v blue)
            time.sleep(0.5)
            #self.toLower(OutgoingChatstateProtocolEntity(OutgoingChatstateProtocolEntity.STATE_TYPING, Jid.normalize(messageProtocolEntity.getFrom(False)) )) #Set is writing
            #time.sleep(2)
            #self.toLower(OutgoingChatstateProtocolEntity(OutgoingChatstateProtocolEntity.STATE_PAUSED, Jid.normalize(messageProtocolEntity.getFrom(False)) )) #Set no is writing
            #time.sleep(1)
            self.onTextMessage(messageProtocolEntity) #Send the answer
            time.sleep(0.5)
            self.toLower(UnavailablePresenceProtocolEntity()) #Set offline
            sys.exit(0)

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        print entity.ack()
        self.toLower(entity.ack())

    def onTextMessage(self,messageProtocolEntity):
        namemitt   = messageProtocolEntity.getNotify()
        message    = messageProtocolEntity.getBody().lower()
        recipient  = messageProtocolEntity.getFrom()
        textmsg    = TextMessageProtocolEntity

        #For a break to use the character \n
        #The sleep you write so #time.sleep(1)
        #answer = "Hi "+namemitt+" " 
        #self.toLower(textmsg(answer, to = recipient ))
        #print answer
        print recipient + ": " +message
