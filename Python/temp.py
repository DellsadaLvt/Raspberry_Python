class clien():
    def __init__(self, clean_section, qos):
        self.clean_section= clean_section
        self.qoss= qos
        
client1= clien( 2, qos= 2)

print(client1.qoss)