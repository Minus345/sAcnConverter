import sacn

if __name__ == '__main__':
    receiver = sacn.sACNreceiver(bind_address='127.0.0.1')
    receiver.start()
    receiver.join_multicast(1)

    sender = sacn.sACNsender(source_name='sAcn Backup',
                             fps=40,
                             bind_address='192.168.178.187')
    sender.start()
    sender.activate_output(1)
    sender[1].multicast = True
    sender[1].priority = 100


    @receiver.listen_on('universe', universe=1)
    def callback(packet):
        sender[1].dmx_data = packet.dmxData
