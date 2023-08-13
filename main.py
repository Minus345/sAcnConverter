import sacn

if __name__ == '__main__':
    receiver = sacn.sACNreceiver()
    receiver.start()
    receiver.join_multicast(1)

    sender = sacn.sACNsender(source_name='sAcn Backup',
                             fps=40,
                             bind_address='192.168.178.131')
    sender.start()
    sender.activate_output(2)
    sender[2].multicast = True
    sender[2].priority = 200


    @receiver.listen_on('universe', universe=1)
    def callback(packet):
        sender[2].dmx_data = packet.dmxData
